from . import views
from django.urls import path, include
from . views import BookListView,BookDetailView,BookReview,BookReserve,AvailableList,BorrowBook,CreateView


urlpatterns = [
    path('register/',views.CreateView.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    path('',BookListView.as_view(),name='booklist'),
    path('detail/<int:pk>/',BookDetailView.as_view(),name='bookdetail'),
    path('review',BookReview.as_view(),name='bookreview'),
    path('reserve',BookReserve.as_view(),name='bookreserve'),
    path('avail',AvailableList.as_view(),name='available'),
    path('borrow/<int:book_id>/',BorrowBook.as_view(),name='borrow'),
]