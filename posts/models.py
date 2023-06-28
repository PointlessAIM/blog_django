from django.db import models
import datetime

from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name="entries")
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.headline
    
    def get_absolute_url(self):
        return redirect(reverse("entries:entry-detail", kwargs={"id": self.id})) #namespace:url_name
    
