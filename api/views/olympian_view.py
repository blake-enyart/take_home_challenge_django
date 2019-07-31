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
        WHERE
            medal IS NOT NULL
        GROUP BY
            name, team, age, sport;
''')

class OlympianList(views.APIView):
    def get(self, request, format=None):
        """
        Return either all or subsets of olympians
        """
        olympians = raw_query # self.get_queryset()

        serializer = OlympianSerializer(olympians, many=True)
        return Response({'olympians': serializer.data})

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = raw_query
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(purchaser__username=username)
    #     return queryset
