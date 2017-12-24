from django.urls import path
from .views import *

app_name = "insta_app"
urlpatterns = [
    path('', post_index, name='post_index'),
    path('add/', post_add, name='post_add'),
    path('<str:slug>/update/', post_update, name='post_update'),
    path('<str:slug>/delete/', post_delete, name='post_delete'),
    path('<str:slug>/', post_details, name='post_details'),
]
