from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.newBook),
    path('addFav', views.favBook),
    path('<int:book_id>', views.showBook),
    path('update', views.updateBook),
    path('delete', views.deleteBook)

]