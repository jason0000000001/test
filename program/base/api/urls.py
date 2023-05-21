from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('users/', views.Users),#讀取所有使用者,創建使用者
    path('users/<str:pk>/', views.updateUser),#讀取,更新,刪除單一使用者(利用 id)
    path('datas/', views.createData),#讀取所有資料,創建資料
    path('datas/<str:pk>/', views.updateData),#讀取,更新,刪除單一資料(利用 id)
    path('<str:pk>/medicine/', views.getmedicine),#讀取單一使用者所有藥品清單(利用 user id)
    path('medicine/', views.createmedicine),#讀取所有藥品清單,創建藥品清單
    path('medicine/<str:pk>/', views.updatemedicine),#讀取,更新,刪除單一藥品清單(利用 id)
    path('datasid/<str:pk>/', views.getDataid),#讀取個人所有資料(利用 user id)
    path('<str:pk>/weight/', views.getweight),#讀取個人所有體重(利用 user id)
    path('<str:pk>/temperature/', views.gettemperature),#讀取個人所有體溫(利用 user id)
    path('<str:pk>/pressures/', views.getpressures),#讀取個人所有收縮壓(利用 user id)
    path('<str:pk>/pressured/', views.getpressured),#讀取個人所有舒張壓(利用 user id)
    path('<str:pk>/heartbeat/', views.getheartbeat),#讀取個人所有心跳(利用 user id)
    path('datastime/<str:pk>/<str:sk>/<str:ek>/', views.getRoomtime),#讀取個人時間範圍內資料(利用 user id)
    path('history/<str:pk>/', views.gethistory),#歷史圖
    path('getmedicine/<str:pk>/', views.get),#查詢藥品資訊
]