from django.shortcuts import render
# Allow other domains to access our API methods
from django.views.decorators.csrf import csrf_exempt
# To Parse the incoming data into data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .models import CustomUserManager
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import json

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


# @csrf_exempt
# def create_user(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)

#         if serializer.is_valid():
#             email = data.get('email')
#             user_password = data.get('user_password')
#             # Remove the email and password from the data to prevent duplication
#             data.pop('email', None)
#             data.pop('user_password', None) 
#             # Ensure remove the password from the data to prevent it from being saved in plain text
#             if 'user_password' in data:
#                 del data['user_password']
#             user = User.objects.create_user(email=email, user_password=user_password, **data)
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         userprofile = User.objects.all()
#         serializer = UserSerializer(userprofile, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
class CreateUser(APIView):

    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            email = data.get('email')
            user_password = data.get('user_password')
            # Ensure to remove the email and password from the data to prevent duplication
            data.pop('email', None)
            data.pop('user_password', None)
            # Ensure to remove the password from the data to prevent it from being saved in plain text
            if 'user_password' in data:
                del data['user_password']
            user = User.objects.create_user(email=email, password=user_password, **data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # get all users' information
    def get(self, request, *args, **kwargs):
        userprofile = User.objects.all()
        serializer = UserSerializer(userprofile, many=True)
        return Response(serializer.data)


# @csrf_exempt
# @login_required  # Ensure the user is logged in
# def retrieve_user_by_pk(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return JsonResponse({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    

#     # get user profile exclude the password from the serialized data
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
    


class RetrieveUserByPK(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class RetrieveLoggedInUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Access the user directly from the request
        user = request.user
        # Check if the user is authenticated
        if user.is_authenticated:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    

# @csrf_exempt
# @login_required  # Ensure the user is logged in
# def update_user_profile(request):
#     if request.method == 'PUT': 

#         data = JSONParser().parse(request)
#         serializer = UserSerializer(request.user, data=data, partial=True)

#         if data.get('email'):
#             return JsonResponse({"detail": "Email cannot be modified."}, status=status.HTTP_400_BAD_REQUEST)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # Handle DELETE request to delete specified contact
#     elif request.method == 'DELETE':
#         request.user.delete()
#         return JsonResponse({'message': 'User was deleted successfully!'}, status=204)
    
class UserProfileUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        data = request.data

        if data.get('email'):
            return Response({"detail": "Email cannot be modified."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(request.user, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        request.user.delete()
        return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

# @csrf_exempt
# @login_required  # Ensure the user is logged in
# def reset_password(request):
#     if request.method == 'PUT': 

#         # get the json data from fronted request
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(request.user, data=data, partial=True)
#         old_password = data.get('old_password')
#         # password authentication with user email
#         user = authenticate(request, email = request.user.email, password = old_password)

#         #authentication pass and tell fronted to enter new passsword, otherwise fail
#         if user is not None:
#             if serializer.is_valid():
#                 # reset password
#                 if data.get('new_password'):
#                     request.user.set_password(data.get('new_password'))
#                     request.user.save()
#                     # Remove the password from the data to prevent it from being saved in plain text
#                     del data['new_password']
#                 serializer.save()
#                 return JsonResponse({'message' : "Password has been changed!"}, status=status.HTTP_201_CREATED)
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return JsonResponse({'message': "The old password you entered does not match our records. Please try again."}, 
#                                 status=status.HTTP_404_NOT_FOUND)
    

class ResetPassword(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        if user.check_password(old_password):
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({'message': "Password has been changed!"}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
    

# @csrf_exempt
# def user_login(request):
#     if request.method == 'POST':
#         # get the json data from fronted request
#         fronted_data = json.loads(request.body.decode('utf-8'))
#         email = fronted_data['email']
#         password = fronted_data['password']
#         #password authentication with user email
#         user = authenticate(request, email = email, password=password)
        
#         #activate user and send response to fronted if authentication pass, otherwise fail
#         if user is not None:
#             login(request, user)
#             # prevent the password leakage
#             del password
#             return JsonResponse({'message' : "You have successfully logged in."}, status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse({'message': "The email and password you entered do not match our records. Please try again."}, 
#                                 status=status.HTTP_401_UNAUTHORIZED)
#     elif request == 'DELETE':
#         logout(request)
#         return JsonResponse({'message': "User logout success!"}, 
#                                 status=status.HTTP_201_CREATED)
    

class Login(APIView):
    ###### DELETE and LOGOUT - did not achieve
    authentication_classes = []
    permission_classes = [AllowAny]
    #@method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "message": 'Logged in successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED) 

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # simply delete the token to force a login
        request.auth.delete()
        return Response({"message": 'Logged out successfully!'}, status=status.HTTP_200_OK)   