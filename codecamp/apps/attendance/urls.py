from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'attendance/(?P<id>\d+)', views.attendance, name='attendance'),
    path('admin/', views.admin, name='admin'),
    re_path(r'^admin/forms/(?P<type>\w+)/add', views.form_add, name='form'),
    re_path(r'^admin/forms/(?P<type>\w+)/edit/(?P<id>\d+)', views.form_edit, name='form'),
]