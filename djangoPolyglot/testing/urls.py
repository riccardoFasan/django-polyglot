from django.urls import path
from testing import views

urlpatterns = [
    path("", views.test, name="test"),
]
