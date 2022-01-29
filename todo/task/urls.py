from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('delete-task/<str:pk>', views.delete_task, name='delete_task'),
    path('edit-task/<str:pk>', views.edit_task, name='edit_task'),
    path('register/', views.create_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    
]
