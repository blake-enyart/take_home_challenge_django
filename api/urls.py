from django.urls import path, re_path
from . import views

urlpatterns = [
    path('olympians/', views.OlympianList.as_view(), name='olympians'),
]
