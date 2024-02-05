from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-id']
        # ordering by id instead of created_at, smart lol
        # no no i was seriou
        # :sunglasses: