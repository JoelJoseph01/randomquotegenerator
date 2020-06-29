from django.db import models

# Create your models here.
class Qu(models.Model):
    quotes=models.CharField(max_length=400)

    def __str__(self):
        return self.quotes