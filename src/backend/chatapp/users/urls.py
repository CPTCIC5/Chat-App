from django.urls import path
from . import views
urlpatterns = [
    #path('register/',views.register,name='register'),
    path('register/',views.RegisterUserAPI.as_view()),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
    
]