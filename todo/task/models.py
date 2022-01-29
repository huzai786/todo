from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    choices = (
        ('Completed', 'Completed'),
        ('In Complete', 'In Complete'),
    )
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    task = models.CharField(max_length=200, null=False, blank=False)
    time = models.TimeField(auto_now_add=False, blank=True)
    status = models.CharField(max_length=200, choices=choices, null=True, blank=False)
    
    
    def __str__(self):
        return self.task


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='pfp.png')
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name