from django.db import models

# Create your models here.
#(ID, Name, Email, password
class User(models.Model):

    Name = models.CharField(max_length=99)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)

    def __str__(self):
        return f"Name: {self.Name}, email: {self.Email} "

#(ID, Name, Image, description)
class Product(models.Model):

    Name = models.CharField(max_length=100)
    Image =  models.CharField(max_length=1000)
    Description = models.CharField(max_length=50)
    def __str__(self):
        return f"Name: {self.Name}, Description: {self.Description} "


