from math import sqrt
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
import json


class ListUserView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListFibonnaciView(generics.ListAPIView):
    """
    Provides a get method handler.
    """

    def get(self, request, number):
        print(number)
        return(Response(json.dumps(fibo(number))))


def fibo(number):
    if (number == 1):
        return [0, 1]
    else:
        s = fibo(number - 1)
        s.append(s[len(s) - 1] + s[len(s) - 2])
        return s


def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
