from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ['id', 'amount', 'product']


class ItemCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ['amount', 'order', 'product']


class StatusSerializer(serializers.ModelSerializer):

	class Meta:
		model = Status
		fields = ['id', 'name']



class OrderSerializer(serializers.ModelSerializer):
	status = StatusSerializer()
	data_order = ItemSerializer(many=True, read_only=True)


	class Meta:
		model = Order
		fields = ['id', 'number', 'status', 'created_at', 'data_order']



class StatusCreateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Status
		fields = ['id']


class OrderCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['status', 'created_at']


