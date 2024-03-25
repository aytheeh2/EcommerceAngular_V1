from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from shop.serializers import CategorySerializer,ProductSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from rest_framework import mixins,generics,viewsets
from django.http import Http404
from rest_framework import status
# def allcategories(request):
#     c=Category.objects.all()
#     return render(request,'category.html',{'c':c})

# @api_view(['GET'])
# def allcategories(request):
#     if(request.method=="GET"):
#         c=Category.objects.all()
#         cat=CategorySerializer(c,many=True)
#         return Response(cat.data)
# class allcategories(APIView):
#     def get(self,request):
#         c = Category.objects.all()
#         cat=CategorySerializer(c,many=True)
#         return Response(cat.data)

# class allcategories(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer
#     def get(self,request):
#         return self.list(request)
# class allcategories(generics.ListAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer
class allcategories(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
# def allproducts(request,p):
#     c=Category.objects.get(name=p)
#     p=Product.objects.filter(category=c)
#     return render(request,'product.html',{'c':c,'p':p})


class allproducts(APIView):
    def get_object(self, request,pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request,pk):
        c = self.get_object(request,pk)
        p=Product.objects.filter(category=c)
        prod=ProductSerializer(p,many=True,context={"request":request})

        return Response(prod.data)

# def detail(request,p):
#     p=Product.objects.get(name=p)
#     return render(request,'detail.html',{'p':p})
class detail(APIView):
    def get_object(self, request,pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request,pk):
        p = self.get_object(request,pk)

        prod=ProductSerializer(p,context={"request":request})

        return Response(prod.data)


# def register(request):
#     if(request.method=="POST"):#After form submission
#         u=request.POST['u']
#         p=request.POST['p']
#         cp=request.POST['cp']
#         fname=request.POST['f']
#         lname=request.POST['l']
#         e=request.POST['e']
#         if(p==cp):
#             user=User.objects.create_user(username=u,password=p,first_name=fname,last_name=lname,email=e)
#             user.save()
#             return redirect('shop:allcat')
#         else:
#             return HttpResponse("Passwods are not same")
#     return render(request,'register.html')

class CreateUser(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

# class CreateUser(APIView):
#     def post(self,request):
#         u=UserSerializer(data=request.data)
#         if(u.is_valid()):
#             u.save()
#             return Response(u.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# def user_login(request):
#     if(request.method=="POST"):
#         u=request.POST['u']
#         p=request.POST['p']
#         user=authenticate(username=u,password=p)
#         if user:
#             login(request,user)
#             return redirect('shop:allcat')
#         else:
#             return HttpResponse("Invalid Credentials")
#     return render(request,'login.html')
# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('shop:login')


class user_logout(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



