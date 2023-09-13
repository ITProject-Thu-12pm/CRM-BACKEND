from django.shortcuts import render
# Allow other domains to access our API methods
from django.views.decorators.csrf import csrf_exempt
# To Parse the incoming data into data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from contact.models import Contact
# Create your views here.
def contact_list(request):
    # Handle GET request to list all contacts
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)
    # Handle POST requests to create new contacts
    elif request.method == 'POST':
        # Parse the JSON data in the request
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():   
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) 