from django.urls import path
from command import views

urlpatterns = [
    path('', views.test, name='test'),
]
