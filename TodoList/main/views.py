from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializers
from .models import Todo


# Create your views here.
@api_view(['GET'])
def goHome(request):
    message = 'You are in the home page'
    return Response(message)

@api_view(['GET'])
def getAlltodos(request):
    todos = Todo.objects.all()
    serializedData = TodoSerializers(todos, many=True)
    return Response(serializedData.data)