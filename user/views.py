from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from user import serializers
# Create your views here.


class LodinUserInfoView(GenericAPIView):

    serializer_class = serializers.LodinUserInfoSerializer

    permission_classes = (IsAuthenticated, )

    def get_object(self):
        print(self.request.user)
        return self.request.user
