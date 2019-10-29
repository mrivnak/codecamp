from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^forms/(?P<type>\w+)/(?P<action>\w+)', views.form, name='form'),
]