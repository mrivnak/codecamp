from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'attendance/(?P<id>\d+)', views.attendance, name='attendance'),
    path('admin/', views.admin, name='admin'),
    re_path(r'^admin/forms/(?P<type>\w+)/(?P<action>\w+)', views.form, name='form'),
]