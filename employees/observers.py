from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee

@receiver(post_save, sender=Employee)
def send_new_employee_notification(sender, instance, created, **kwargs):
    if created:
        # Send a notification about the new employee to the admin users
        pass
