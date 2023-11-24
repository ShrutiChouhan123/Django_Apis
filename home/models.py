from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self) -> str:
        return self.name  + ' ' + self.email