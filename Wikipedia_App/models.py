from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 20)
    defination = models.CharField(max_length = 2000)
    details = models.CharField(max_length = 10000)

    def __str__(self):
        return self.name
