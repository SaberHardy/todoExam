from django.shortcuts import render
#rest frame work
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required 
from rest_framework import viewsets
from . import models
from . import serializers



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks,many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	
	if serializer.is_valid():
		serializer.save()
	
	return Response(serializer.data)

@login_required
@api_view(['POST'])
def taskUpdate(request,pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.TaskSerializer

# @api_view(['POST',])
# def api_create(request):
#     todo = ToDo.objects.get(id=1)
#     blog_post = ToDo(author=todo)
#     if request.method == "POST":
#     	serializer = TaskSerializer(blog_post,data=request.data)
#     	data={}
#     	if serializer.is_valid():
#     		serializer.save()
#     		return Response(serializer.data,status=status.HTTP_201_CREATE)
#     	return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    
