from django.urls import path
from . import views

urlpatterns = [
    # Function Based
    path('', views.trainee_list, name='trainee_list'),
    path('<int:pk>/', views.trainee_detail, name='trainee_detail'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('update/<int:pk>/', views.update_trainee, name='update_trainee'),
    path('delete/<int:pk>/', views.delete_trainee, name='delete_trainee'),
    path('soft-delete/<int:pk>/', views.soft_delete_trainee, name='soft_delete_trainee'),

    # Class Based View
    path('add-cbv/', views.AddTraineeCBV.as_view(), name='add_trainee_cbv'),

    # Generic Views
    path('generic/', views.TraineeListGeneric.as_view(), name='trainee_list_generic'),
    path('add-generic/', views.TraineeCreateGeneric.as_view(), name='add_trainee_generic'),
]