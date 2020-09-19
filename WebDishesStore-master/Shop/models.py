from django.db import models
from django.utils.html import mark_safe


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f"tag={self.tag}"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"subcategory={self.name}"


class Product(models.Model):
    name = models.CharField(max_length=2048)
    desc = models.TextField()
    tag = models.ManyToManyField(Tag)
    subCategory = models.ManyToManyField(SubCategory)

    def __str__(self):
        return f"prod = {self.name}"


class Sale(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    coef = models.FloatField()

    def __str__(self):
        return f"prod = {self.prod.name}, sale coefficient={self.coef}"


class Category(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"prod = {self.prod.name}, category={self.name}"


class Photo(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/photos')

    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="200" height="200" />')

    def __str__(self):
        return f"prod = {self.prod.name}, img name={self.img.name}"


class Cart(models.Model):
    name = models.CharField(max_length=2048)
    surname = models.CharField(max_length=2048)
    address = models.TextField()
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"bayer = {self.name} {self.surname}, prod = {self.prod.name}, amount = {self.amount}, address={self.address}"


class Article(models.Model):
    title = models.CharField(max_length=2048)
    subTitle = models.CharField(max_length=2048)
    text = models.TextField()

    def __str__(self):
        return f"title = {self.title}, subtitle = {self.subTitle}"
