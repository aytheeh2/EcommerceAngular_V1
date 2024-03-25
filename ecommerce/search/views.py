from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from shop.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# def search(request):
#     query=""
#     products=None
#     if(request.method=="POST"):
#         query=request.POST['q']
#         if(query):
#             products=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
#
#     return render(request,'search.html',{'query':query,'p':products})


class search(APIView):
    def get(self,request):
        #to get the keyword for search from the request query parameters send from client
        query=self.request.query_params.get('search') #{params:{'search':'carrot}} #default key search
        if (query):
             products=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
             p=ProductSerializer(products,many=True,context={"request":request})
             return Response(p.data)







