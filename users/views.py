from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import UserSerializer, UserPhotoSerializer
from django.db.models import Q

# Create your views here.


class UserViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        queryset = queryset.filter(Q(id=self.request.user.id))
        return queryset



class UserPhotoViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = UserPhotoSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        queryset = queryset.filter(Q(id=self.request.user.id))
        return queryset