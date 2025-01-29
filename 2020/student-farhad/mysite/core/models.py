from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    picture = models.ImageField(upload_to='product_pics')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name} - {self.price}'

