from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "product"
        ordering = ['name']
        verbose_name_plural = "products"
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
class Address(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    telephone_number = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Address"
        ordering = ['name']
        verbose_name_plural = "Addressses"    

class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product.name
    class Meta:
        db_table = "AddToCard"
        ordering = ['product']
        verbose_name_plural = "AddToCards"
    def get_absolute_url(self):
        return reverse("card", kwargs={"pk": self.pk})
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name
    class Meta:
        db_table = "Review"
        ordering = ['product']
        verbose_name_plural = "Reviews"
    def get_absolute_url(self):
        return reverse("review", kwargs={"pk": self.pk})
                    
class Category(models.Model):
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(	Product)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "Category"
        ordering = ['name']
        verbose_name_plural = "Categories"
    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})