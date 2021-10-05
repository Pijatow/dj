from django.db import models

# Create your models here.


class Product(models.Model):
    def __str__(self):
        return f'{self.name} -> {self.seller}'
    name = models.CharField(max_length=30)
    seller = models.CharField(max_length=60)
    price = models.IntegerField(default=True)
    creation_time = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now_add=True, null=True)
