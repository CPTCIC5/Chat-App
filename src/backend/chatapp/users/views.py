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

#k
@api_view(['POST']) # only allows POST requests
def register(request):
    if request.method == 'POST':

        serializer= UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # this return the error if the serializer is not valid
        # if serializer.is_valid():
        if serializer.validated_data.get("password") == serializer.validated_data.get("confirm_password"):
            #print('xyzz',serializer.validated_data.get("password"),serializer.validated_data.get("confirm_password"))

            serializer.validated_data.pop("confirm_password") #Delete confirm_password before saving the data
            serializer.save()
            userr= authenticate(request,username=request.data['username'],password=request.data['password'])
            auth_login(request,userr)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        # if you are returning an error, the http status code gotta be some error status code
        # the status code should me appropriate
        # so yeah 400 bad request is appropriate for this case, but 404 not found isn't,  ok
        return Response("Password and Confirm-Password didnt match",status=status.HTTP_400_BAD_REQUEST)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # views always gotta return a Response object, can't return a normal string
    # return('not post') # is wrong
    return Response('Not post')
    # but theres no point in this, since you ONLY allow POST requsts in the first place
    #makes sense.


"""
class RegisterUserAPI(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
"""

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            user = authenticate(request,**login_serializer.data)
            if user is  None:
                return Response({'detail': 'Account with the given credentials does not exist'},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif not user.is_active:
                return Response({'detail': 'User is not active'}, status=status.HTTP_401_UNAUTHORIZED)
            auth_login(request,user)
            return Response(login_serializer.data,status=status.HTTP_201_CREATED)
        return Response('login hogya')

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # same thing here
    # views only can return Response objects
    # return "Logged out" # wrong
    return Response("logged out")
