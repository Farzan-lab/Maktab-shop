from django.urls import path
from . import views


urlpatterns = [
    path('add-order/',views.create_order,name="add-order"),
]