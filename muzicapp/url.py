from .views import *
from django.urls import path

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
     path('create/', Create.as_view(), name='create' ),
    path('detail/<int:pk>/', Detail.as_view() ,name='detail'  ),
     path('update/<int:pk>/', Update.as_view(),name='update'  ),
     path('delete/<int:pk>/', Delete.as_view(),name='delete'  ),


]
