from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.signup, name='signup'),
    path('delete', views.delete, name='delete_data'),
]
