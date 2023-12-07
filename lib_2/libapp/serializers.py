from rest_framework import serializers
from . models import *
from django.contrib.auth import get_user_model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class ReserveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self,validated_data):
        user=get_user_model().objects.create(
            username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

