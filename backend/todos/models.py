from django.db import models
from phone_field import PhoneField


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    address = models.TextField(max_length=140, default='default')
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.title
