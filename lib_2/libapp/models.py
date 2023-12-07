from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=250)
    b_author = models.CharField(max_length=250)
    b_desc = models.TextField()
    b_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    def __str__(self):
        return self.b_name
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    def __str__(self):
        return f"{self.user.username} reviewed {self.book.b_name}"
class Reserve(models.Model):
    reserve_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.b_name
