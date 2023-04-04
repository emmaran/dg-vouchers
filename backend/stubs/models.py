from django.db import models

# Create your models here.

class Bank(models.Model):
    cardNum = models.FloatField

    def float (self):
        return self.cardNum

        