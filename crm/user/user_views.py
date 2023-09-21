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
import json

from .serializers import UserSerializer

# # Create your views here.
# @csrf_exempt
# def userProfile_list(request):
#     # Handle GET request to list all contacts
#     if request.method == 'GET':
#         userprofile = UserProfile.objects.all()
#         serializer = UserProfileSerializer(userprofile, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     # Handle POST requests to create new contacts
#     elif request.method == 'POST':
#         # Parse the JSON data in the request
#         data = JSONParser().parse(request)
#         serializer = UserProfileSerializer(data=data)
#         if serializer.is_valid():   
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400) 
    

# @csrf_exempt
# def user_detail(request, pk):
#     # Attempts to obtain the specified contact
#     try:
#         userProfile =UserProfile.objects.get(pk=pk)
#     except UserProfile.DoesNotExist:
#         return JsonResponse({'error': 'user not found'}, status=404)

#     # Handle GET request to obtain the details of the specified contact
#     if request.method == 'GET':
#         serializer = UserProfileSerializer(userProfile)
#         return JsonResponse(serializer.data)

#     # Process the PUT request and update the specified contact information
#     elif request.method == 'PUT':
#         # Parse the JSON data in the request
#         data = JSONParser().parse(request)
#         serializer = UserProfileSerializer(userProfile, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     # Handle DELETE request to delete specified contact
#     elif request.method == 'DELETE':
#         userProfile.delete()
#         return JsonResponse({'message': 'user was deleted successfully!'}, status=204)

##################################


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            email = data.get('email')
            user_password = data.get('user_password')
            # print(user_password)
            # Remove the email and password from the data to prevent duplication
            data.pop('email', None)
            data.pop('user_password', None) 
            # Remove the password from the data to prevent it from being saved in plain text
            if 'user_password' in data:
                del data['user_password']
            user = User.objects.create_user(email=email, user_password=user_password, **data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        userprofile = User.objects.all()
        serializer = UserSerializer(userprofile, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def retrieve_user_by_email(request, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    

    # Exclude the password from the serialized data
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    ##########################################
    # need to change to login require
    elif request.method == 'POST':
        # get the json data from fronted request
        data = JSONParser().parse(request)
        old_password = data.get('password')
        #password authentication with user email
        user = authenticate(request, email = email, password = old_password)
        
        #authentication pass and tell fronted to enter new passsword, otherwise fail
        if user is not None:
            return JsonResponse({'message' : "Allow to change new password!"}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': "The old password you entered does not match our records. Please try again."}, 
                                status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT': 

        data = JSONParser().parse(request)
        # data = json.loads(request.body.decode('utf-8'))
        serializer = UserSerializer(user, data=data, partial=True)

        if data.get('email'):
            return JsonResponse({"detail": "Email cannot be modified."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            if data.get('user_password'):
                user.set_password(data.get('user_password'))
                # print(data.get('user_password'))
                user.save()
                # Remove the password from the data to prevent it from being saved in plain text
                del data['user_password']
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Handle DELETE request to delete specified contact
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=204)

########################
# @csrf_exempt
# def update_user_profile(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return JsonResponse({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


#     # Parse the JSON data in the request
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(user, data=data, partial=True)

#         if request.data.get('email'):
#             return JsonResponse({"detail": "Email cannot be modified."}, status=status.HTTP_400_BAD_REQUEST)

#         if serializer.is_valid():
#             if data.get('user_password'):
#                 user.set_password(data.get('user_password'))
#                 user.save()
#                 # Remove the password from the data to prevent it from being saved in plain text
#                 del data['user_password']
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        # get the json data from fronted request
        fronted_data = json.loads(request.body.decode('utf-8'))
        email = fronted_data['email']
        password = fronted_data['password']
        #password authentication with user email
        user = authenticate(request, email = email, password=password)
        
        #activate user and send response to fronted if authentication pass, otherwise fail
        if user is not None:
            login(request, user)
            # prevent the password leakage
            del password
            return JsonResponse({'message' : "You have successfully logged in."}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': "The email and password you entered do not match our records. Please try again."}, 
                                status=status.HTTP_404_NOT_FOUND)
    elif request == 'DELETE':
        logout(request)
        return JsonResponse({'message': "User logout success!"}, 
                                status=status.HTTP_201_CREATED)