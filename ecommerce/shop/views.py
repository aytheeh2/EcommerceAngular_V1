from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from shop.models import Category, Product
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from shop.serializers import CategorySerializer, ProductSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from rest_framework import mixins, generics, viewsets, status


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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# def allproducts(request,p):
#     c=Category.objects.get(name=p)
#     p = Product.objects.filter(category=c)
#     return render(request,'product.html',{'c':c,'p':p})

# Class based View API :

class allproducts(APIView):
    def get_object(self, request, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        c = self.get_object(request, pk)
        p = Product.objects.filter(category=c)
        prod = ProductSerializer(p, many=True, context={"request": request})

        return Response(prod.data)

# def detail(request,p):
#     d = Product.objects.get(name=p)
#     return render (request,'detail.html',{'d':d})

# class detail(APIView):      #Class based Function
#     def get_object(self,request,pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except:
#             raise Http404
#     def get(self,request,pk):
#         p = self.get_object(request, pk)
#         prod=ProductSerializer(p)
#
#         return Response(prod.data)

# class detail(generics.RetrieveAPIView):   #primary keybased  --------By using Generics View
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class detail(mixins.RetrieveModelMixin,generics.GenericAPIView): #primary keybased  --------By using Mixins View
#
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)


class detail(viewsets.ModelViewSet):  # --------By using  Viewset Function
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# def register(request):
#     if (request.method == "POST"):
#         u=request.POST['us']
#         p=request.POST['ps']
#         cp=request.POST['cp']
#         fname=request.POST['fn']
#         lname=request.POST['ln']
#         em=request.POST['em']
#
#
#         if (p==cp):
#             user=User.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=em)
#             user.save()
#             return redirect('shop:allcat')
#         else:
#             return HttpResponse("Passwords are not same")
#
#     return render(request,'register.html')

class CreateUser(viewsets.ModelViewSet):  # --------By using  Viewset Function
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def userlogin(request):
#     if(request.method=="POST"):
#         u=request.POST['us']
#         p=request.POST['ps']
#         user=authenticate(username=u,password=p)    #buit in function
#         if user:
#             login(request,user)
#             return redirect('shop:allcat')
#         else:
#             return HttpResponse("invalid credential")
#
#     return render(request,'login.html')

# class userlogin(APIView):
#     def post(self,request):
#         u=UserSerializer(data=request.data)
#         if(u.is_valid()):
#             u.save()
#             return Response(u.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# @login_required
# def userlogout(request):
#     logout(request)
#     return redirect('shop:userlogin')


class userlogout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
