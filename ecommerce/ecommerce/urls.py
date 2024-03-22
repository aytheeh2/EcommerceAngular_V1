"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from shop import views
from django.conf.urls.static import static
from rest_framework.authtoken import views as rviews         #import aliasing

from rest_framework.routers import SimpleRouter
router=SimpleRouter()

router.register('cat',views.allcategories)    #path-------http://127.0.0.1:8000/shop/cat/      path koduthakunnathu    ( path('shop/',include(router.urls)),)
router.register('detail',views.detail)          #path-------http://127.0.0.1:8000/shop/detail/1/
router.register('user',views.CreateUser)        #path-------http://127.0.0.1:8000/shop/user/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('search/',include('search.urls')),
    path('cart/',include('cart.urls')),
    path('shop/',include(router.urls)),
    path('api-token-auth/',rviews.obtain_auth_token),       #login view

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)