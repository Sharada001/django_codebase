from django.db import models

# Create your models here.
class Food(models.Model) :
    code = models.IntegerField()
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2,max_digits=20)
