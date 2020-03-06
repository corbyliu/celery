from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from django.views.decorators.vary import vary_on_headers
from user import serializers
from user.models import User
# Create your views here.


class LodinUserInfoView(GenericAPIView):

    serializer_class = serializers.LodinUserInfoSerializer

    permission_classes = (IsAuthenticated, )

    def get_object(self):
        print(self.request.user)
        return self.request.user


class CreateUser(GenericAPIView):

    queryset = User.objects.all()

    @vary_on_headers('User-Agent')
    def get(self, request):

        obj_user = self.get_queryset()
        print(obj_user)
        return JsonResponse({"data": "ok"})

    def post(self, request):

        data = request.data
        username = data.get("username")
        password = data.get("password")
        user_info = User.objects.create_user(username=username, password=password)
        return JsonResponse({"data": "ok"})

    def put(self, request):

        data = request.data
        user_id_list = data.get("user_id")
        params_data = data.get("user_info")
        for user_id in user_id_list:
            user_info = User.objects.modify_user(user_id, **params_data)
        return JsonResponse({"data": "ok"})

    def delete(self, request):

        data = request.data
        user_id_list = data.get("user_id")
        for user_id in user_id_list:
            User.objects.delete_user(user_id)
        return JsonResponse({"data": "ok"})
