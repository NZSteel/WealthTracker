from django.urls import path
from investmentrecorder import views

urlpatterns = [
    path('', views.index, name='index')

]