from django.conf.urls import url
from . import views
app_name = 'main'
urlpatterns = [
    url(r'^$', views.home,name='home'),
    
    url(r'^solicitud/$', views.solicitud,name='solicitud'),
    url(r'^senda/$', views.senda),
       
]
