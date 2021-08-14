import django_filters.rest_framework
from rest_framework import generics
from .models import Messages
from .serializers import MessageSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


# Create your views here.
class MessageListView(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields =['sender','recipient']

class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    def create(self,request,*args,**kwargs):
        message_data = request.data
        sender_id = message_data["sender"]
        recipient_id = message_data['recipient']
        print(User.objects.filter(id=sender_id).values())
        new_message = Messages.objects.create(
            sender_id = message_data["sender"],
            recipient_id = message_data['recipient'],
            message = message_data['message'],
        )
        new_message.save()
        serializer = MessageSerializer(new_message)
        return Response(serializer.data)