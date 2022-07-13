from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(max_length=300)
    image = models.ImageField(upload_to="profile/images", blank=True, null=True)
    slug = models.SlugField(max_length=255, db_index=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name} {self.last_name}")
        return super().save(*args, **kwargs)