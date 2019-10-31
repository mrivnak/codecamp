from django.urls import path, re_path

from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    re_path(r'^admin/forms/(?P<type>\w+)/(?P<action>\w+)', views.form, name='form'),
]