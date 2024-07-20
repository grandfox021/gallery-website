from django.urls import path

from pictures import views

urlpatterns = [
    
path('',views.display_all_pictures,name='all_pictures'),
path('uploadfile/<pk>',views.upload_pic,name='upload_file'),
path('view_photo/<str:pk>', views.view_picture ,name='view_photo'),


]





