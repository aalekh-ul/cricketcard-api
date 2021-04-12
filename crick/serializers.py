from django.db.models import fields
from rest_framework import serializers
from .models import players,tt


class ttSerializer(serializers.ModelSerializer):
    class Meta():
        model=tt
        fields= ('player','runs','wickets','strikrate','matches','hundreds','avg','economy')
        depth=1