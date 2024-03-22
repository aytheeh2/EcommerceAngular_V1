
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from shop import views
app_name = "shop"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.allcategories,name="allcat"),
    path('allproducts/<int:pk>/', views.allproducts.as_view(),name="allproducts"),  # http://127.0.0.1:8000/detail/1/
    # path('detail/<int:pk>',views.detail.as_view(),name="detail"),
    # path('userlogin', views.userlogin, name="userlogin"),
    # path('register', views.register, name="register"),
    path('logout', views.userlogout.as_view(), name="logout"),


]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
