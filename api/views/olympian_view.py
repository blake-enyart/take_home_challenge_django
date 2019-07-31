from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from ..models import Olympian
from ..serializers import OlympianSerializer

raw_query = Olympian.objects.raw('''
    SELECT ROW_NUMBER() OVER(ORDER BY name) AS id,
        name, team, age, sport,
        COUNT(medal) AS total_medals_won
        FROM api_olympian
        GROUP BY
            name, team, age, sport;
''')

class OlympianList(views.APIView):
    def get(self, request, format=None):
        """
        Return either all or subsets of olympians
        """
        olympians = self.get_queryset()

        serializer = OlympianSerializer(olympians, many=True)
        return Response({'olympians': serializer.data})

    def get_queryset(self):
        """
        Optionally restricts the returned olympians,
        by filtering against an `age` query parameter in the URL.
        """
        queryset = raw_query
        age = self.request.query_params.get('age', None)
        if age is not None:
            if age == 'youngest':
                queryset = Olympian.objects.raw("""
                    SELECT *
                        FROM
                            (SELECT DENSE_RANK() OVER(ORDER BY age) AS id,
                                name, team, age, sport,
                                COUNT(medal) AS total_medals_won
                                FROM api_olympian
                                GROUP BY
                                    name, team, age, sport) AS subq
                        WHERE id = 1;
                """)
            elif age == 'oldest':
                queryset = Olympian.objects.raw("""
                    SELECT *
                        FROM
                            (SELECT DENSE_RANK() OVER(ORDER BY age DESC) AS id,
                                name, team, age, sport,
                                COUNT(medal) AS total_medals_won
                                FROM api_olympian
                                GROUP BY
                                    name, team, age, sport) AS subq
                        WHERE id = 1;
                """)
        return queryset
