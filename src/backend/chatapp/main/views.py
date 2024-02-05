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
remove this
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
#using consumers.py to serve this but made this for practice. <- ???
# also for this its better to use viewsets instead of APIView --ok
class MessageAPI(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,format=None):
        # maybe in the future consinder implementing pagination?
        query= Message.objects.all()
        serializer = MessageSerializer(query, many=True)
        return Response(serializer.data)
    
    
    def post(self,request,format=None):
        serializerr = MessageSerializer(data=request.data)
        serializerr.is_valid(raise_exception=True)

        serializerr.save(author=request.user)
        return Response(serializerr.data,status=status.HTTP_201_CREATED)
    
    

    def put(self,request,pk,format=None):
        obj = get_object_or_404(Message,pk=pk)
        serializier= MessageSerializer(obj, data=request.data, partial=False)
        serializier.is_valid(raise_exception=True)

        serializier.save()
        return Response(serializier.data)
    
    def delete(self,request,pk,format=None):
        obj = get_object_or_404(Message,pk=pk)
        # maybe allow staff users to delete other peoples messages if u want to -- makes sense
        if request.user == obj.author:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
