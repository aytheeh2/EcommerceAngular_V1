

from rest_framework import serializers
from cart.models import Cart, Order


class CartSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField('sub')
    image = serializers.SerializerMethodField('getimage')
    name = serializers.SerializerMethodField('getname')
    price = serializers.SerializerMethodField('getprice')
    user = serializers.SerializerMethodField('getuser')
    
    

    class Meta:
        model = Cart
        fields = '__all__'

    def sub(self, obj):
        subtotal = obj.product.price*obj.quantity
        return subtotal

    def getname(self, obj):
        return obj.product.name

    def getimage(self, obj):
        i_url = obj.product.image.url
        # return request.build_absolute_uri(i_url)
        return obj.product.image.url
    
    def getprice(self,obj):
        return obj.product.price
    
    def getuser(self,obj):
        return obj.user.username


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'no_of_items', 'user', 'ordered_date',
                  'address', 'phone', 'order_status', 'delivery_status']
