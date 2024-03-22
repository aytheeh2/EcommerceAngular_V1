from django.contrib.auth.models import User
from rest_framework import serializers


from shop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'desc', 'image']


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Product
        fields = ['id', 'name', 'desc', 'image', 'price',
                  'stock', 'category', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get("request")
        i_url = obj.image.url
        return request.build_absolute_url(i_url)


class UserSerializer(serializers.ModelSerializer):
    # Password hide chythu veykn use chyunne code
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):  # after validation      (password Encrypted)
        u = User.objects.create_user(
            username=validated_data['username'], password=validated_data['password'])
        u.save()
        return u
