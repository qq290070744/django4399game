from django.db import models

# Create your models here.
class youxi(models.Model):
    name=models.CharField(max_length=550)
    imgurl=models.CharField(max_length=999)
    flashurl=models.CharField(max_length=500)

    def __str__(self):
        return  self.name

