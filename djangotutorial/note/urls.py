from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"), 
    # # path("note/<int:note_id>/", views.detail, name="detail"),
    # path('note/directory/', views.index, name='directory_list'),  # แสดงรายการจาก Desktop
    # path('note/directory/<path:path>/', views.index, name='directory_list_with_path'),  # เข้าถึงโฟลเดอร์ภายใน

    path('', views.index, name='directory'),
    path('<path:path>/', views.index, name='directory')
]
