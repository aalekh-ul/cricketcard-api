from http.client import ImproperConnectionState
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework import  status
from . models import players, tt
from . serializers import  ttSerializer
from crick import serializers
import random

def home(requests):
    return HttpResponse("<h1>hello</h1>")


class playerlist(APIView):
    def get(self,request):
          
            w=tt.objects.all()
            wserializer=ttSerializer(w,many=True)
            result=wserializer.data
            return Response(result)


class random_playerlist(APIView):
    def get(self,request):
            
            item=list(tt.objects.all())
            item=random.sample(item,10)
            wserializer=ttSerializer(item,many=True)
            result=wserializer.data
            return Response(result)







