from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainee_list, name='trainee_list'),
    path('<int:pk>/', views.trainee_detail, name='trainee_detail'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('update/<int:pk>/', views.update_trainee, name='update_trainee'),
    path('delete/<int:pk>/', views.delete_trainee, name='delete_trainee'),
]