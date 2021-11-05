from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Prefetch




class Orders(APIView):
	lookup_url_kwarg = 'id'

	def get(self, request):
		orders = Order.objects.all()
		data = OrderSerializer(orders, many=True).data
		return Response(data, status=200)

	def post(self, request):
		data = Order.objects.create()
		serialized_data = OrderSerializer(data).data
		return Response(serialized_data, status=200)

	def put(self, request):
		id = request.GET.get(self.lookup_url_kwarg)
		if id is not None:
			order = Order.objects.get(id=id)
			serialized_data = OrderCreateSerializer(order, data=request.data)
			if serialized_data.is_valid():
				serialized_data.save()
				return Response(serialized_data.data)
			return Response(serialized_data.errors, status=400)
		return Response({'Bad request': 'ID parameter not found in request!'}, status=400)

	def delete(self, request):
		id = request.GET.get(self.lookup_url_kwarg)
		if id is not None:
			order = Order.objects.get(id=id)
			order.delete()
			serialized_data = OrderSerializer(Order.objects.all(), many=True)
			return Response(serialized_data.data)
		return Response({'Bad request': 'ID parameter not found in request!'}, status=400)


class OrderDetail(APIView):

	def get(self, request, id):
		try:
			project = Order.objects.get(id=id)
			data = OrderSerializer(project).data
			result = Item.objects.filter(order=project).values_list('product', 'amount')
			return Response(data, status=200)
		except:
			return Response({'Bad request': 'ID parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)


class ListOfStatus(APIView):

	def get(self, request):
		statuts = Status.objects.all()
		data = StatusSerializer(statuts, many=True).data
		return Response({"result": data}, status=200)


class AddProductToOrder(APIView):
	lookup_url_kwarg = 'id'
	def post(self, request):
		serialized_data = ItemCreateSerializer(data=request.data)
		if serialized_data.is_valid():
			serialized_data.save()
			return Response("created!", status=200)
		return Response(serialized_data.errors)

	def delete(self, request):
		item_id = request.GET.get(self.lookup_url_kwarg)
		item = Item.objects.get(id=item_id)
		item.delete()
		return Response("deleted", status=200)





