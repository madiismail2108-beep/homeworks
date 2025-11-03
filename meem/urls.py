from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-book/', views.add_book, name='add-book'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/<int:pk>/update/', views.update_book, name='update-book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete-book'),
]
