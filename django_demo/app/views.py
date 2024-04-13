from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, filters
from .models import Rooms

from .serializers import RoomSerializers

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

@api_view(['GET', 'POST'])
def getrooms(request):
    if request.method == 'GET':
        rooms = Rooms.objects.all()
        roomserializer = RoomSerializers(rooms, many = True)
        return Response(roomserializer.data)
    if request.method == 'POST':
        request_data = request.data
        serialize_request_data = RoomSerializers(data = request_data)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message" : "Added Successfully"})

class RoomList(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializers

    filter_backends = [filters.SearchFilter]
    search_fields = ['id']