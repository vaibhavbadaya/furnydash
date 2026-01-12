from django.db import models

# reate your models here.


class Brand(models.Model):
    
    id = models.BigAutoField(primary_key = True)
    name=models.CharField(max_length=128)
    email=models.EmailField(max_length=128,null=True,blank=True)
    contact=models.CharField(max_length=128,null=True,blank=True)
    headoffice=models.CharField(max_length=128,null=True,blank=True)

    class Meta:
        db_table="brand_management"

    def __str__(self):
        return f"{self.name}"


