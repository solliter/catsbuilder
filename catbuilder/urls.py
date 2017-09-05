from django.conf.urls import url, include
from . import views




urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^new/$', views.new_cat, name='new_cat'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.cat_edit, name='cat_edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.cat_delete, name='cat_delete'),





]

