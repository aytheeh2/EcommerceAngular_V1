from django.contrib.auth.models import User
from rest_framework import serializers
from shop.models import Category,Product
class CategorySerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=Category
        fields=['id','name','desc','image']


class ProductSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
    image_url=serializers.SerializerMethodField('get_image_url')
    class Meta:
        model=Product
        fields=['id','name','desc','image','price','stock','image_url']

    def get_image_url(self,obj):
        request=self.context.get("request")
        i_url=obj.image.url
        return request.build_absolute_uri(i_url)


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','password']

    def create(self,validated_data):#after validation
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u