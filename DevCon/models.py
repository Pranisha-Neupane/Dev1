from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class Room(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    created_by=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
class Message(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now_add=True)
    body=models.TextField(null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)

class Participents(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    room_id=models.CharField(max_length=200)
    



