from django.urls import path, include

from accounts import views

urlpatterns = [
    path('users/new/', views.Register.as_view(), name='user-create'),
    
    path('users/<int:pk>/', views.UserView.as_view(), name='retrieve'),
    path('users/<int:pk>/update/', views.UserView.as_view(), name='update'),
    path('users/<int:pk>/delete/', views.UserView.as_view(), name='delete'),
]