from django.shortcuts import render

def about(request):
    return render(request, 'api/about.html', {})
