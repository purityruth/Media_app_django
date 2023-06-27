from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    # path('products/', views.products, name="products"),
    path('user/', views.user, name="user"),

    path('create_media/', views.createMedia, name="create_media"),
    path('update_media/<str:pk>/', views.updateMedia, name="update_media"),
    path('delete_media/<str:pk>/', views.deleteMedia, name="delete_media")
]