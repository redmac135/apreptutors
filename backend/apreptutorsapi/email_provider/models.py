from django.db import models
from django.utils import timezone

# Create your models here.
class EmailRecord(models.Model):
    time_sent = models.DateTimeField(auto_now_add=True)
    sender = models.EmailField()
    reciever = models.EmailField()
    body = models.CharField(max_length=2048)