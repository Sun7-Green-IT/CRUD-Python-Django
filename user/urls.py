from django.urls import path
from .views import ListUserView, ListFibonnaciView


urlpatterns = [
    path('users/', ListUserView.as_view(), name="user-all"),
    path('fibonnaci/<int:number>/',
         ListFibonnaciView.as_view(), name="fibonnaci-all")
]
