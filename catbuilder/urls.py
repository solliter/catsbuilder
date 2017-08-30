from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new/$', views.new_cat, name='new_cat'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.cat_edit, name='cat_edit'),


]

