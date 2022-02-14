from django.db.models.signals import post_save
from .models import User
from django.dispatch import receiver
from . models import Profile



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = Profile.objects.create(user=instance)