from rest_framework import serializers
from userprofile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields=('first_name', 'last_name', 'date_of_birth', 'address', 'city', 'state', 
                'zip_code', 'user_email', 'user_password', 'phone')