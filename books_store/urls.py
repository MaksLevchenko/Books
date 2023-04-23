from django.urls import path

from books_store import views


urlpatterns = [
    path('books/', views.BooksListView.as_view(), name='create'),
    path('book/<int:pk>/', views.UpdateBookView.as_view(), name='update'),
    path('book-del/<int:pk>/', views.DeleteBookView.as_view(), name='delete'),
    path('action/', views.ActionView.as_view(), name='action'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
