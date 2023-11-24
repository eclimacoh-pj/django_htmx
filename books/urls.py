from django.urls import path

from .views import *


app_name = 'books'
urlpatterns = [
    path('', index, name='index'),
    path('libros', book_list, name='book_list'),
    path('libros/nuevo/', add_book, name='add_book'),
    path('libros/<int:pk>/eliminar/confirmacion/', delete_book_confirmation, name='delete_book_confirmation'),
    path('libros/<int:pk>/eliminar/', delete_book, name='delete_book'),
    path('libros/<int:pk>/actualizar/', edit_book, name='edit_book'),
]
