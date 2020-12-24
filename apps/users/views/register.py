from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import collections


class GetSmsApiView(APIView):

    def get(self, mobile):
        # 1，先生成随机的六位数验证码
        # 2，打印验证码用于测试
        # 3，生成redis储存字段
        # 4，存入redis中以供验证使用
        pass


class RegisterApiView(APIView):

    pass
