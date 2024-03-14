from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='pdf_files'),
    path('upload/', views.upload_file, name='upload_file'),
    path('delete/<int:id>/', views.delete_file, name='delete_file'),
    path('delete/', views.delete_all_files, name='delete_all_files'),

]