from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=10, null=True)
    email=models.CharField(max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # password=<PASSWORD>(max_length=20)

    def __init__(self, name):
        self._name = name

class Media(models.Model):
    TYPE = (
        ('Video', 'Video'),
        ('Audio', 'Audio'),
        ('Image', 'Image'),
    )
    file_name = models.CharField(max_length=250, null=True)
    file_type = models.CharField(max_length=250, null=True, choices=TYPE)
    file_url = models.CharField(max_length=800, null=True)

    def __str__(self):
        return self.file_name