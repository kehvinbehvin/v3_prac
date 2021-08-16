from .models import First
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import FirstSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class FirstViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = First.objects.all()
    # The serializer class for serializing output
    serializer_class = FirstSerializer
    # optional permission class set permission level
    permission_classes = [IsAuthenticated] #Coule be [permissions.IsAuthenticated]  
    
    