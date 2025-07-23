from django.db import models
from django.db.models.fields import BigIntegerField


class Category(models.Model):
    name = models.CharField(max_length=100)
    products_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Password(models.Model):
    password = models.CharField(max_length=100)

    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        related_name='password_info',)

    def __str__(self):
        return self.password


# author = Author.objects.get(id=1)
# print(author.password_info.password)



# 6 - task

class User(models.Model):
    user_id=BigIntegerField()
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    qr_code_image = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return f'{self.full_name} - {self.email}'



