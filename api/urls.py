from django.urls import path,include
# from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()

# router.register('shop', views.ShopView, basename='shop')

urlpatterns = [
    path('',views.ShopView.as_view()),
    path('shop/<int:pk>/',views.ShopView.as_view()),
    # path('auth/',include('rest_framework.urls')),

]
