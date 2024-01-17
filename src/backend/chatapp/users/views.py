from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserCreateSerializer,LoginSerializer
from rest_framework  import generics
from rest_framework.permissions  import IsAuthenticated

"""
@api_view(['GET','POST'])
def register(request):
    if request.method == 'POST':
        serializer= UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('not post')
"""


class RegisterUserAPI(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
     

@api_view(['GET','POST'])
def login(request):
    if request.method == 'POST':
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user = authenticate(request,**login_serializer.data)
        if user is  None:
            return Response({'detail': 'Account with the given credentials does not exist'},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if not user.is_active:
             return Response({'detail': 'User is not active'}, status=status.HTTP_401_UNAUTHORIZED)
        auth_login(request,user)
        return Response('login hogya')

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    return "Logged out"