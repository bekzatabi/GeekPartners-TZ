from django.db import models
import string
import random


def generate_unique_code():
    length = 4
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Order.objects.filter(number=code).count() == 0:
            break

    return code


class Status(models.Model):
	name = models.CharField(max_length=120)


	def __str__(self):
		return self.name



class Order(models.Model):
	number = models.CharField(max_length=120, default=generate_unique_code, unique=True)
	status = models.ForeignKey(Status, on_delete=models.SET_NULL, default=1, related_name='data_status', null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.number


class Product(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


class Item(models.Model):
	product = models.CharField(max_length=120, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='data_order', null=True)
	amount = models.IntegerField(default=0)

	def __str__(self):
		return self.product