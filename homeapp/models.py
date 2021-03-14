from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class player(models.Model):
    name = models.CharField(max_length=200)
    points = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.name

# This model is not configured yet
# class points(models.Model):
#     user = models.ForeignKey(player, on_delete=models.CASCADE)
#     point = models.IntegerField(default=0,blank=True,null=True)
