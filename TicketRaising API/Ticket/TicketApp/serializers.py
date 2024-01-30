from rest_framework import serializers
from .models import *

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'