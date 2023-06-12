from django.urls import path, include
from .views import *

urlpatterns = [

    path('users', UserListApiView.as_view()),
    path('users/<int:user_id>', UserDetailApiView.as_view()),

    path('books', BookListApiView.as_view()),
    path('books/<int:book_id>', BookDetailApiView.as_view()),

    path('authors', AuthorListApiView.as_view()),
    path('authors/<int:author_id>', AuthorDetailApiView.as_view())

]
