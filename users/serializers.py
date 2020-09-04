from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,
                            get_username_max_length)

from .models import User


UPLOADED_FILES_USE_URL= 'http://s3-us-east-1.amazonaws.com/backend-group-hackathon/'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'country', 'street_address', 'city')

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    street_address = serializers.CharField(max_length=300, allow_blank=True, required=False)
    country = serializers.CharField(max_length=300, allow_blank=True, required=False)
    city = serializers.CharField(max_length=300, allow_blank=True, required=False)
    photo = serializers.FileField(max_length=None, allow_empty_file=True,
        use_url=UPLOADED_FILES_USE_URL, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password','photo', 'street_address', 'city','country')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'photo': self.validated_data.get('photo', ''),
            'street_address': self.validated_data.get('street_address', ''),
            'country': self.validated_data.get('country', ''),
            'city': self.validated_data.get('city', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.street_address = self.cleaned_data.get('address')
        user.country = self.cleaned_data.get('country')
        user.city = self.cleaned_data.get('city')
        user.photo = self.cleaned_data.get('photo')
        user.save()
        adapter.save_user(request, user, self)
        print(user)
        return user
