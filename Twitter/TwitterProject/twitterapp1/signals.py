from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
        
        
        
import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Post

@receiver(post_delete, sender=Post)
def delete_image_on_post_delete(sender, instance, **kwargs):
    if instance.image and instance.image.name:
        try:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
        except Exception as e:
            print("Error deleting image after post delete:", e)

@receiver(pre_save, sender=Post)
def delete_old_image_on_image_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # It's a new post; skip

    try:
        old_post = Post.objects.get(pk=instance.pk)
    except Post.DoesNotExist:
        return  # No previous instance; skip

    old_image = old_post.image
    new_image = instance.image

    # ⚠️ Skip if image is unchanged
    if not old_image or not old_image.name:
        return

    if new_image and old_image.name != new_image.name:
        try:
            if os.path.isfile(old_image.path):
                os.remove(old_image.path)
        except Exception as e:
            print("Error deleting old image:", e)
