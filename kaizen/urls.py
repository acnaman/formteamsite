from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^$', views.index, name='index'),
]