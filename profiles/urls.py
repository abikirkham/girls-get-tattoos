from django.urls import path
from . import views
from .views import liked_items_view

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('liked_items/', liked_items_view, name='liked_items'),
]