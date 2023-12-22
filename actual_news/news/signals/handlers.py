from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf.urls.static import static
from .. import models

@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, **kwargs):
    if kwargs['created']:
        models.Profile.objects.create(user=kwargs['instance'])