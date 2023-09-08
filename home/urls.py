from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('',index, name = "home"),
    path('signin',signin, name = "signin"),
    path('signup',signup, name = "signup"),
    path('found_items',findPage, name = "found_items"),
    path('thankyou',RecievedPage, name = "thankyou"), 
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/create/', ItemCreateView.as_view(), name='item-create'),  # Add this line
]

