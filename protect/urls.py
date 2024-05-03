from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from protect.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),

]