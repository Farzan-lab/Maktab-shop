from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('orders/', views.OrderListView.as_view(), name="orders"),
    path('order-detail/<int:pk>/', views.OrderDetailView.as_view(), name="order-detail"),
    path('logout/', auth_views.LogoutView.as_view(template_name='customers/logout.html'), name='logout'),
]