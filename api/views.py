from django.db.models import query
from django.http import JsonResponse
from rest_framework import generics, views
from rest_framework.response import Response
from django.core.paginator import Paginator
from .serializers import YoutubeAPISearchSerializer
from .models import Videos
# from .serializers import YoutubeAPISearchSerializer

# <=========Views Here=========>
class YoutubeAPIHomeView(views.APIView):
   def get(self, request, format=None):
      return Response({
      "success": True,
      "message": "Hello from the server!"
    })

class YoutubeAPISearchView(generics.ListAPIView):
   serializer_class = YoutubeAPISearchSerializer
   queryset = Videos.objects.all().order_by('-publishing_time')