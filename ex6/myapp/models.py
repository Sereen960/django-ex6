from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

