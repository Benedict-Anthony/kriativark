from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.caption


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=50)
    excert = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    


class Comments(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name_plural = "Comments"