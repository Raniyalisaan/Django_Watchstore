from django.db import models



class Product(models.Model):
    productName = models.CharField(max_length=100)
    productDescription = models.TextField()
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productPhoto = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.productName