from django.urls import re_path
from blog_app import views

urlpatterns = [
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
]
