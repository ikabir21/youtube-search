from django.urls import path
from .views import *

urlpatterns = [
     path('', YoutubeAPIHomeView.as_view(), name="home")
]
