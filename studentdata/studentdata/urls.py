from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.user_login,name = 'login'),
    path('logout',views.logoutuser,name = 'logout'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update_data'),
    path('updatenew/<int:id>/', views.update_new, name='update_new'),
    path('delete/<int:id>/', views.deletedata, name='delete_data'),
    path('register/', views.registerPage,name ='register')
]