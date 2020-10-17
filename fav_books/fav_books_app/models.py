from django.db import models
from login_reg.models import *

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user_who_posted = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    users_who_liked = models.ManyToManyField(User, related_name="books_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
