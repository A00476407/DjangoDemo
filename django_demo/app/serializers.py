from rest_framework import serializers
from .models import Rooms

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        #fields = ['id', 'price', 'type_id']
        fields = "__all__"