from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User

from rest_framework import generics

from .serializers import UserSerializer, ProfileSerializer, PaymentSerializer
from .models import Profile, Payment


# --- Users --- 
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail2(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


# --- Profile ----
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        if self.kwargs.get('user_pk') is not None:
            return self.queryset.filter(user_id=self.kwargs.get('user_pk'))
        return self.queryset.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# --- Payment ---
class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        if self.kwargs.get('user_pk') is not None:
            return self.queryset.filter(user_id=self.kwargs.get('user_pk'))
        return self.queryset.all()


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer