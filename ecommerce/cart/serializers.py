


from rest_framework import serializers
from cart.models import Cart,Order
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['id','product','quantity','user']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'no_of_items', 'user','ordered_date','address','phone','order_status','delivery_status']