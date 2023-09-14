from rest_framework import serializers
from contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=('contact_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'address', 
                'phone_number', 'email')