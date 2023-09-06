from django.db import models
from django.contrib.auth.models import User
from product.models import Product 
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    


 # Replace with your Card model if needed

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)  

    def __str__(self):
        return f'Wishlist of {self.user.username}'


  


