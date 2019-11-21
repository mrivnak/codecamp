from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'attendance/(?P<id>\d+)', views.attendance, name='attendance'),
    path('attendance/', views.attendance_basic, name='attendance'),
    path('data/', views.data_user, name='data'),
    path('admin/', views.admin, name='admin'),
    path('admin/data/', views.data, name='data'),
    re_path(r'^admin/forms/(?P<type>\w+)/add', views.form_add, name='form_add'),
    re_path(r'^admin/forms/(?P<type>\w+)/edit/(?P<id>\d+)', views.form_edit, name='form_edit'),
    re_path(r'^admin/forms/(?P<type>\w+)/delete/(?P<id>\d+)', views.delete, name='delete')
]