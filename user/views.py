# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            confirm_password = serializer.validated_data['confirm_password']

            if password == confirm_password:
                # Create a new user
                user = User.objects.create_user(username=username, password=password)

                # Optionally, you may want to log in the user after registration
                # login(request, user)

                return Response({"message": "User registered successfully"})
            else:
                return Response({"error": "Passwords do not match"}, status=400)
        return Response(serializer.errors, status=400)
        
        
# from django.contrib.auth import authenticate, login
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import UserSerializer

# class LoginUserView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return Response({"message": "Login successful"})
#         else:
#             return Response({"error": "Invalid credentials"}, status=401)

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({"message": "Login successful", "access_token": access_token})
        else:
            return Response({"error": "Invalid credentials"}, status=401)