from django import views
from django.urls import path
from .views import MyTokenObtainPairView, category_list, category_detail, product_list, product_detail, members


urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('login/', MyTokenObtainPairView.as_view()),
    path('members/', members, name='members'),
    
]
