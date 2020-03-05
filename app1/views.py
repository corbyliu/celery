from django.shortcuts import render
from app1.tasks import add
from django.views import View
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
# Create your views here.


class TestView(GenericAPIView):

    def get(self, request):

        params = request.query_params
        # x = params.get("x")
        # y = params.get("y")
        # r = add.delay(int(x), int(y))
        # task_id = r.id
        # print(task_id)
        return JsonResponse({"data": "123"})
