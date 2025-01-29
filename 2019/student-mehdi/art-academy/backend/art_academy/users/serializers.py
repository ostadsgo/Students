from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('__all__')


class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = ('__all__')
