from django.shortcuts import render
from .models import Blog
from rest_framework import status
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

"""
    #
    # Class Based Views
    #
"""
# GET, POST Request Accepted  
class BlogListView(APIView):
    def get(self, request):
          blogs = Blog.objects.filter(is_public=True)
          serializer = BlogSerializer(blogs, many=True)
          return Response(serializer.data,  status=status.HTTP_200_OK)
    def post(self, request):
         serializer = BlogSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,  status=status.HTTP_200_OK)
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, DELETE Request Accepted       
class BlogDetailView(APIView):
    def get(self, request, pk):
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    def put(self, request, pk):
        blog = Blog.objects.get(is_public=True, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        blog = Blog.objects.get( pk=pk)
        blog.delete()
        return Response()
    
         
          
         
"""
    #
    # Function Based Views
    #
"""
# @api_view(['GET','POST'])
# def blog_list(request):
#     if request.method == "GET":
#         blogs = Blog.objects.filter(is_public=True)
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data,  status=status.HTTP_200_OK)
#     if request.method == "POST":
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,  status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def blog_detail(request, pk):
#     if request.method == "GET":
#         blogs = Blog.objects.filter(is_public=True, pk=pk)
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data,  status=status.HTTP_200_OK)
#     if request.method == "PUT":
#         blog = Blog.objects.get(is_public=True, pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,  status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         blog = Blog.objects.get( pk=pk)
#         blog.delete()
#         return Response()