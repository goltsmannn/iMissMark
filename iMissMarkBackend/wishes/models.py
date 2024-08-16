from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Wish(models.Model):
    text = models.TextField()
    publication_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Text: {self.text}, Author: {self.author}"