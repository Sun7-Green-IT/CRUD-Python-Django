from django.urls import path
from .views import ListUserView


urlpatterns = [
    path('user/', ListUserView.as_view(), name="user-all")
]
