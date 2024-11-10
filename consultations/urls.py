from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_consultations, name='consultations'),
    path('<int:consultation_id>/', views.consultation_detail, name='consultation-detail'),
    path('add/', views.add_consultation, name='add_consultation'),
    path('edit/<int:consultation_id>/', views.edit_consultation, name='edit_consultation'),
    path('delete/<int:consultation_id>/', views.delete_consultation, name='delete_consultation'),
]