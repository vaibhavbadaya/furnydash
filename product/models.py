from django.db import models
from brand.models import Brand


class Category(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=128)
    descrption = models.CharField(max_length=50)
    brand = models.ForeignKey(to=Brand,on_delete=models.CASCADE)

    class Meta:
        db_table="category_management"

    def __str__(self):
        return f"{self.name}"

# Create you
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand =models.ForeignKey(to=Brand,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table="product_management"


    # def __str__(self):
        # return self.namer models here.
