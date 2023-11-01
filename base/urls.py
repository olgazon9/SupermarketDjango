from django.urls import path
from .views import (
    MyTokenObtainPairView,
    CategoryList,
    CategoryDetail,
    ProductList,
    ProductDetail,
    members,
    user_register,
)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('members/', members, name='members'),
    path('register/', user_register, name='user-register'),
]
