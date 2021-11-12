from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 255)
    num_pages = models.IntegerField(default=0)
    isbn = models.CharField(max_length=13, blank = True, null = True)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(blank = True, null = True, decimal_places = 2, max_digits = 25)


    def __str__(self):
        return self.title



