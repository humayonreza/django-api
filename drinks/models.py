from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=30)
    des = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " - " + self.des