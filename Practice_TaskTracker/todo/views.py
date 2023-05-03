from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def welcome(request):
    return HttpResponse('<h1 style="background-color: blanchedalmond">Welcome</h1>')
    
@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
        
        
    elif request.method == 'POST':#
        serializer = TodoSerializer(todos, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         
        

def todo_update_delete():
    pass