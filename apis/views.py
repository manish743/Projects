from django.shortcuts import render
from .serializers import TodoSerializer, RegisterSerializer, UserSerializer, LoginSerializer
from .models import Todo
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import views
from django.contrib.auth import authenticate, login

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    if request.method == "GET":
        todos = Todo.objects.filter(user = request.user)
        serializer = TodoSerializer(todos, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk = pk, user = request.user)
    except Todo.DoesNotExist:
        return Response(status = status.HTTP_400_NOT_FOUND)
    
    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)