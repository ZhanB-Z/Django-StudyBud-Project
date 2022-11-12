from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # on_delete part means that if the room is deleted all the children (messages) are also deleted
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #this to show when the room was last updated
    created = models.DateTimeField(auto_now_add=True) #this to show when the room was created


    class Meta:
        ordering = ['-updated','-created'] #this line orders rooms in the order with newest (updates/created) rooms first


    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # on_delete part means that if the room is deleted all the children (messages) are also deleted
    body = models.TextField()

    updated = models.DateTimeField(auto_now=True)  # this to show when the room was last updated
    created = models.DateTimeField(auto_now_add=True) #this to show when the room was created

    class Meta:
        ordering = ['-updated', '-created'] #this line orders rooms in the order with newest (updates/created) rooms first

    def __str__(self):
        return self.body[0:50]