from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class ChatRoom(models.Model):

    name = models.CharField(max_length=100)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class ChatMassages(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    massage_content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('date', )

    def __str__(self) -> str:
        return self.user.username + ' send in room: ' + self.room.name
