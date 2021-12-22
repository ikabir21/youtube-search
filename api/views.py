from django.http import JsonResponse
from rest_framework import generics, serializers, views
from rest_framework.response import Response
# from .serializers import YoutubeAPISearchSerializer

# <=========Views Here=========>
class YoutubeAPIHomeView(views.APIView):
   def get(self, request, format=None):
      return Response({
      "success": True,
      "message": "Hello from the server!"
    })
