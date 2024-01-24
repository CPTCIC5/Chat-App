#from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework  import generics
from .models import Message
from rest_framework.views import APIView

"""
@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET','POST'])
def message(request):
    if request.method == 'GET':

        query= Message.objects.all()
        serializer = MessageSerializer(query,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        
        print('aaaya')
        if request.user.is_authenticated:
            data= {"author":request.user.id,"text":request.data.get("text")}
            serializerr= MessageSerializer(data=data)
            if serializerr.is_valid():
                serializerr.save()
                return Response(serializerr.data,status=status.HTTP_201_CREATED)
            return Response(serializerr.errors, status=status.HTTP_400_BAD_REQUEST)
"""

class MessageAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,format=None):
        query= Message.objects.all()
        serializer = MessageSerializer(query, many=True)
        return Response(serializer.data)
    
    
    def post(self,request,format=None):
        data= {"author":request.user.id,"text":request.data.get("text")}
        serializerr = MessageSerializer(data=data)
        if serializerr.is_valid():
            serializerr.save()
            return Response(serializerr.data,status=status.HTTP_201_CREATED)
        return Response(serializerr.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    def put(self,request,pk,format=None):
        obj = get_object_or_404(Message,pk=pk)
        data= {"author": obj.author,"text":request.data.get("text",obj)}
        serializier= MessageSerializer(data=data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data)
        return Response(serializier.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        obj = get_object_or_404(Message,pk=pk)
        if request.user == obj.author:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
