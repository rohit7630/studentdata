from django.urls import path, include
from data import views

urlpatterns = [
    path('form/', views.add, name="add"),
    path('index/', views.index, name="index"),
    path('update/<int:id>/', views.update, name="update_data"),
    path('delete/<int:id>/', views.delete, name="delete_data"),
]


