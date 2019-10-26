from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve

from webshop import settings
from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    url(r'^images/(?P<path>.*)$', serve, {'document_root': 'shopapp/static/images'}),
    url(r'^js/(?P<path>.*)$', serve, {'document_root': 'shopapp/static/js'}),
    url(r'^switcher/(?P<path>.*)$', serve, {'document_root': 'shopapp/static/switcher'}),
    url(r'^fonts/(?P<path>.*)$', serve, {'document_root': 'shopapp/static/fonts'}),
    url(r'^css/(?P<path>.*)$', serve, {'document_root': 'shopapp/static/css'}),
#    path('bestsellurl', views.bestsell),
    url(r'^$', views.index, name='index'),
]
