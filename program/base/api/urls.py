from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),#房間列表
    path('rooms/<str:pk>/', views.getRoom),#讀取房間
    path('createrooms', views.createRoom),#新增房間
    path('updaterooms/<str:pk>/', views.updateRoom),#更新房間
    path('deleterooms/<str:pk>/', views.deleteRoom),#刪除房間
]
