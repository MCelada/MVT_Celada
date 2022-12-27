from django.db import models

# Create your models here.
class Listar(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    number = models.IntegerField()
    it_lives = models.BooleanField()
    



    