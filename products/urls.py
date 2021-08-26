from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(),name="home-page"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(),name="product-detail")
]