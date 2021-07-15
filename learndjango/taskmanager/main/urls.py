from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index , name='main_page'),
    path('about-us',  views.about, name='about_us'),
    path('book/create/', BookCreate.as_view(), name='book_create_url'),
    path('book/<str:slug>/', BookDetail.as_view(), name='book_detail_url'),
    path('book/<str:slug>/update/', BookUpdate.as_view(), name='book_update_url'),
    path('book/<str:slug>/delete/', BookDelete.as_view(), name='book_delete_url'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]