from django.conf.urls import patterns, url
from bandit import views

urlpatterns = patterns('', 
               url(r'^$', views.index, name='index'),
               url(r'^register/$', views.register, name='register'),
               url(r'^login/$', views.user_login, name='login'),
               url(r'^restricted/', views.restricted, name='restricted'),
               url(r'^logout/$', views.user_logout, name='logout'),
               url(r'^event/(?P<event_name_slug>[\w\-]+)/$', views.event, name='event'),
               url(r'^band/(?P<profile_name_slug>[\w\-]+)/$', views.band, name='band'),
               url(r'^venue/(?P<profile_name_slug>[\w\-]+)/$', views.venue, name='venue'),
               url(r'^event/(?P<event_name_slug>[\w\-]+)/request/(?P<profile_name_slug>[\w\-]+)/$', views.request, name='request'),
               )