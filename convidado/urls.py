from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_convidados),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalhe),
    url(r'^post/new/$', views.novo_convidado, name='novo_convidado'),
    url(r'^mapa', views.mapa_casamento),
]