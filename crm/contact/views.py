from django.shortcuts import render
# Allow other domains to access our API methods
from django.views.decorators.csrf import csrf_exempt
# To Parse the incoming data into data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import ContactSerializer



from contact.models import Contact
# Create your views here.
@csrf_exempt
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
    

@csrf_exempt
def contact_detail(request, pk):
    # Attempts to obtain the specified contact
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return JsonResponse({'error': 'Contact not found'}, status=404)

    # Handle GET request to obtain the details of the specified contact
    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return JsonResponse(serializer.data)

    # Process the PUT request and update the specified contact information
    elif request.method == 'PUT':
        # Parse the JSON data in the request
        data = JSONParser().parse(request)
        serializer = ContactSerializer(contact, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    # Handle DELETE request to delete specified contact
    elif request.method == 'DELETE':
        contact.delete()
        return JsonResponse({'message': 'Contact was deleted successfully!'}, status=204)