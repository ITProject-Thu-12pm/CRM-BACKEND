from django.shortcuts import render
from .serializers import EventSerializer

from .models import Event

from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EventCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data=request.data
        frontend_start = data.get("start", None)  # or whatever the key for the date is in your JSON

        if frontend_start:
            # Convert the frontend date string to a datetime object
            date_obj1 = datetime.strptime(frontend_start, '%d-%m-%Y').date()

            # Convert the datetime object to the desired string format
            backend_start = date_obj1.strftime('%Y-%m-%d')

            # Update the date in your request data
            data["start"] = backend_start

        frontend_end = data.get("end", None)  # or whatever the key for the date is in your JSON

        if frontend_end:
            # Convert the frontend date string to a datetime object
            date_obj2 = datetime.strptime(frontend_end, '%d-%m-%Y').date()

            # Convert the datetime object to the desired string format
            backend_end = date_obj2.strftime('%Y-%m-%d')

            # Update the date in your request data
            data["end"] = backend_end

        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Retrieve, Update, and Delete
class EventRetrieveUpdateDestroyView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return None

    def get(self, request, pk):
        event = self.get_object(pk)
        if event is None:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        if event is None:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        frontend_start = data.get("start", None)  # or whatever the key for the date is in your JSON

        if frontend_start:
            # Convert the frontend date string to a datetime object
            date_obj1 = datetime.strptime(frontend_start, '%d-%m-%Y').date()

            # Convert the datetime object to the desired string format
            backend_start = date_obj1.strftime('%Y-%m-%d')

            # Update the date in your request data
            data["start"] = backend_start

        frontend_end = data.get("end", None)  # or whatever the key for the date is in your JSON

        if frontend_end:
            # Convert the frontend date string to a datetime object
            date_obj2 = datetime.strptime(frontend_end, '%d-%m-%Y').date()

            # Convert the datetime object to the desired string format
            backend_end = date_obj2.strftime('%Y-%m-%d')

            # Update the date in your request data
            data["end"] = backend_end

        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = self.get_object(pk)
        if event is None:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)