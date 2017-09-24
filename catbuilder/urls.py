from django.conf.urls import url, include
from . import views
from .views import new_cat, cat_detail



urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^create/$', new_cat),

    url(r'^new/$', views.new_cat, name='new_cat'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.cat_edit, name='cat_edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.cat_delete, name='cat_delete'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<pk>[0-9]+)/$', views.cat_detail, name='cat_detail'),

]

