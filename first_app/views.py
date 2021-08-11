from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FirstSerializer
# Create your views here.


class FirstViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = First.objects.all()
    # The serializer class for serializing output
    serializer_class = FirstSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
    
