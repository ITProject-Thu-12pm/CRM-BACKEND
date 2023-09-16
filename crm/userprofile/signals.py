from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from contact.models import Contact

@receiver(post_save, sender=UserProfile)
def update_corresponding_contact(sender, instance, **kwargs):
    try:
        # Check if there's a corresponding contact with the same email
        contact = Contact.objects.get(email=instance.user_email)
        contact.first_name = instance.first_name
        contact.last_name = instance.last_name
        contact.date_of_birth = instance.date_of_birth
        contact.address = instance.address
        contact.city = instance.city
        contact.state = instance.state
        contact.phone = instance.phone
        # contact.email = instance.email
        
        contact.save()
    except Contact.DoesNotExist:
        pass
