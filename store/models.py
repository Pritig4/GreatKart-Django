from django.db import models
from category.models import category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name  =models.CharField(max_length=50,unique=True)
    slug          =models.SlugField(max_length=50, unique=True)
    descriptions  =models.TextField(max_length=50, blank=True)
    price         =models.IntegerField()
    image         =models.ImageField(upload_to='photos/Products',blank=True)
    stock         =models.IntegerField()

    category      =models.ForeignKey(category ,on_delete=models.CASCADE)
    created_date  =models.DateTimeField(auto_now_add=True)
    modify_date   =models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug , self.slug])

    def __str__(self):
        return self.product_name
