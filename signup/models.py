from django.db import models

# Create your models here.

class Signup(models.Model):
    name        = models.CharField(max_length=120)
    email       = models.EmailField(blank=False, null=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email