from django.contrib import admin
from .models import Message
# Register your models here.
admin.site.register(Message)

# maybe create a ModelAdmin for the message model