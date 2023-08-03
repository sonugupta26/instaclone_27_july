from django.db import models
from django.conf import settings

class PostStatus(models.TextChoices):
    PUBLIC = ("public", "Public")
    PRIVATE = ("private", "Private")

# Create your models here.
class Post(models.Model):
    picture = models.ImageField(upload_to="posts/")
    caption = models.CharField(max_length=255, blank =True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete =models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=100, choices=PostStatus.choices, default=PostStatus.PRIVATE)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "posts"
        
    def __str__(self):
        return str(self.id)
    
class Like(models.Model):
    is_liked = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete =models.SET_NULL, blank=True, null=True)

    
    def __str__(self):
        return str(self.id)
    
    
class Comment(models.Model):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete =models.SET_NULL, blank=True, null=True)

    
    def __str__(self):
        return self.text