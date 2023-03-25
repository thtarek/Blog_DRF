from django.shortcuts import render
from .models import Blog
from rest_framework import status
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def blog_detail(request, pk):
    blogs = Blog.objects.filter(is_public=True, pk=pk)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data,  status=status.HTTP_200_OK)