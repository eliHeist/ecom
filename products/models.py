from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    cartegories = models.ManyToManyField('Cartegory', blank=True)

    def __str__(self):
        return self.name
    
    def actualPrice(self):
        return (self.price*self.discount)/100 if self.discount else self.price
    
    def formatedPrice(self):
        return f"{self.actualPrice():,}"


class Cartegory(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Cartegory'
        verbose_name_plural = 'Cartegories'

    def __str__(self):
        return self.name
