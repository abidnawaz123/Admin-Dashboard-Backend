from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from django.core.mail import send_mail
import os

@receiver(post_delete,sender=User)
def delete_associated_files(sender,instance,**kwargs):
    """Delete the file from the filesystem if it exists"""
    if instance.cv:
        if os.path.isfile(instance.cv.path):
            os.remove(instance.cv.path)

@receiver(post_save,sender=User,dispatch_uid="send_welcome_email")
def send_welcome_email(sender,instance ,created, **kwargs):
    """
    Send a welcome email to the user which has been created
    """
    print("Signal Fired !!")
    if created:
        send_mail(
            "Welcome",
            "Thankyou for signing up",
            "admin@django.com",
            [instance.email],
            fail_silently=False,
        )
