from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput


class Contact_Message(models.Model):
    STATUS = (('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed'))
    name = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
