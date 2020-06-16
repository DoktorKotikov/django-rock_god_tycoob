from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cities/$', views.cities, name='cities'),
    url(r'city/(?P<pk>\d+)', views.citydetail, name='city-detail'),
    url(r'gig/(?P<pk>\d+)', views.gigdetail, name='gig-detail'),
    url(r'^gigs/$', views.gigs, name='gigs'),
    url(r'pub/(?P<pk>\d+)', views.pubdetail, name='pub-detail'),
    url(r'fastfood/(?P<pk>\d+)', views.fastfooddetail, name='fastfood-detail'),
    url(r'hospital/(?P<pk>\d+)', views.hospitaldetail, name='hospital-detail'),
    url(r'strip/(?P<pk>\d+)', views.stripdetail, name='strip-detail'),
    url(r'^entertainments/$', views.entertainments, name='entertainments'),
    url(r'^recorddeals/$', views.recorddeals, name='recorddeals'),
    url(r'^recordstudios/$', views.recordstudios, name='recordstudios'),
    url(r'^videoclip/$', views.videoclip, name='videoclip'),
    url(r'^recorddeals/(?P<pk>\d+)', views.recorddealsdetail, name='recorddeals-detail'),
    url(r'^recordstudios/(?P<pk>\d+)', views.recordstudiosdetail, name='recordstudios-detail'),
    url(r'^videoclip/(?P<pk>\d+)', views.videoclipdetail, name='videoclip-detail'),


]