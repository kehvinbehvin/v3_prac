from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender_c_id')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_id')
    message = models.CharField(max_length=200)

    # def __str__(self):
    #     return f"Sender:{self.sender}, Recipient:{self.recipient}, message:{self.message}"