from django.urls import path, include
from . import views 
from rest_framework import routers 

router=routers.DefaultRouter()
router.register('address', views.CustomerAddressViewset)
router.register('productrating', views.ProductRatingViewset)

urlpatterns = [
    path('vendors/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),

    path('customers/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),

    path('orders/', views.OrderList.as_view()),
    path('order-detail/<int:pk>/', views.OrderDetail.as_view()),
]

urlpatterns+=router.urls