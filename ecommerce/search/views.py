from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Product

from shop.serializers import ProductSerializer


# Create your views here.

# def search(request):               #function based
#     query = ""
#     b = None
#     if request.method == "POST":
#         query = request.POST.get('q', '')
#         if query:
#             b = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
#     return render(request, "search.html", {'query': query, 'b': b})


class search(APIView):
    def get(self,request):
        #to get the keyword for search from request query parameters send from client
        query=self.request.query_params.get('search')   #{params:{'search':'carrot}} default search key
        if(query):
            b = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
            p=ProductSerializer(b,many=True)
            return Response(p.data)
