from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.shortcuts import redirect
from django.urls import reverse

class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})
    
    def get_like_url(self):
        return reverse("posts:like", kwargs={"slug": self.slug})
    
    @property
    def comments(self):
        return self.comment_set.all().order_by('-timestamp')
    @property
    def get_comment(self):
        return self.comment_set.all().count()

    @property
    def get_like(self):
        return self.like_set.all().count()
    
    @property
    def get_view(self):
        return self.postview_set.all().count()
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.user.username
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
