from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
def welcome(request):
    return HttpResponse('idsbu9snais')


from rest_framework import viewsets, permissions
from .models import Profile, Post, Comment, Like
from .serializers import (
    RegisterSerializer, ProfileSerializer, PostSerializer,
    CommentSerializer, LikeSerializer
)
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.parsers import MultiPartParser, FormParser

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()                                                                                       
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  # ✅ REQUIRED for image upload

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this post.")
        serializer.save()




        


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
        



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userdatasender(request):
    user = request.user
    return Response({
        'user': {
            'id': user.id,
            'username': user.username
        }
    })
    
    
    
    
from .models import Profile
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes, permission_classes
from .serializers import ProfileSerializer
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST

@api_view(['PUT', 'PATCH'])
@parser_classes([MultiPartParser, FormParser])  # important for image and form data
@permission_classes([IsAuthenticated])
def update_profile_info(request,pk):
    obj = Profile.objects.get(user_id = pk)
    udata  = request.data
    sobj = ProfileSerializer(instance = obj,data = udata)
    if sobj.is_valid() == True:
        sobj.save()
        return Response(sobj.data,status=HTTP_200_OK)
    
    return Response(sobj.errors,status=HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getpostapi(request,pk):
    d = Post.objects.get(id = pk)
    dobj = PostSerializer(d)
    return Response(dobj.data,status=HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({'message': 'Deleted successfully'}, status=204)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

class CreateCommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Automatically assign logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# views.py
from rest_framework.generics import ListAPIView
from .models import Comment
from .serializers import CommentSerializer

class PostCommentsListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id']).order_by('-created_at')
    
    
    
    
    

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        post_id = request.data.get("post")

        if not post_id:
            return Response({"error": "Post ID is required"}, status=400)

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)

        # Check if the like already exists
        existing_like = Like.objects.filter(user=user, post=post).first()

        if existing_like:
            existing_like.delete()
            return Response({"message": "Unliked successfully"}, status=status.HTTP_204_NO_CONTENT)

        # Create a new like if not exists
        like = Like.objects.create(user=user, post=post)
        serializer = self.get_serializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
