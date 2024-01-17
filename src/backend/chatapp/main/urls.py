from django.urls import path
from . import views


urlpatterns = [
    path('message/',views.MessageAPI.as_view(),name='message'),
]