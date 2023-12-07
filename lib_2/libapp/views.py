from rest_framework.permissions import AllowAny
from . serializers import BookSerializer,ReviewSerializer,ReserveSerializers,UserSerializer
from . models import *
from rest_framework import generics,permissions
from django.contrib.auth import get_user_model

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookDetailView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, serializer):
        serializer.save(user=self.request.user)
class BookReserve(generics.ListAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializers
    permission_classes = [permissions.IsAuthenticated]
    def create(self,serializer):
        serializer.save(user=self.request.user)
class AvailableList(generics.ListAPIView):
    queryset = Book.objects.filter(reserve__isnull=True)
    serializer_class = BookSerializer
class BorrowBook(generics.CreateAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializers
    permission_classes = [permissions.IsAuthenticated]
    def create(self,serializer):
        serializer.save(user=self.request.user)

class CreateView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer