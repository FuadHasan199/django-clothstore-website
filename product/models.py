from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    cat_img = models.ImageField(upload_to='photos/categories',blank = True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/product')
    stock = models.IntegerField()
    size = models.CharField(max_length=15,default='Medium')
    color = models.CharField(max_length=20,null=True)
    is_available = models.BooleanField(default=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_ratings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name

    def update_average_rating(self):
        reviews = self.review_set.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            self.average_rating = total_rating / len(reviews)
            self.total_ratings = len(reviews)
        else:
            self.average_rating = 0.00
            self.total_ratings = 0
        self.save()


class Review(models.Model):
    comment = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=5)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
   

    def __str__(self):
        return self.comment