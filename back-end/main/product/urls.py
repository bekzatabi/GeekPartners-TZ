from django.urls import path
from .views import *


urlpatterns = [
    path('orders', Orders.as_view(), name='orders_urls'),
    path('status', ListOfStatus.as_view()),
    path('order_detail/<int:id>', OrderDetail.as_view()),
    path('add_product', AddProductToOrder.as_view()),
]