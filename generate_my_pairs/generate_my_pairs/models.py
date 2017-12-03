from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def get_absolute_url(self):
        return reverse('home')