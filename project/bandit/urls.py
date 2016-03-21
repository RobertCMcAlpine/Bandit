from django.conf.urls import patterns, url
from bandit import views

urlpatterns = patterns('', 
               url(r'^$', views.index, name='index'),
               url(r'^register/$', views.register, name='register'),
               url(r'^login/$', views.user_login, name='login'),
               url(r'^logout/$', views.user_logout, name='logout'),
               url(r'^band/(?P<band_profile_name_slug>[\w\-]+)/$', views.band, name='band'),
               url(r'^venue/(?P<venue_profile_name_slug>[\w\-]+)/$', views.venue, name='venue'),
               url(r'^venue/(?P<venue_profile_name_slug>[\w\-]+)/event/(?P<event_date_slug>[\d\-]+)/$', views.event, name='event'),
               url(r'^venue/(?P<venue_profile_name_slug>[\w\-]+)/add_event/$', views.add_event, name='add_event'),
               url(r'^venue/(?P<venue_profile_name_slug>[\w\-]+)/event/(?P<event_date_slug>[\d\-]+)/request/(?P<band_profile_name_slug>[\w\-]+)/$', views.request, name='request'),
               url(r'^make_gig_request/$', views.make_gig_request, name='make_gig_request'),
               url(r'^accept_gig_request/$', views.accept_gig_request, name='accept_gig_request'),
               url(r'^events/$', views.events, name='events'),
               url(r'^bands/$', views.bands, name='bands'),
               url(r'^venues/$', views.venues, name='venues'),
               url(r'^band/(?P<band_profile_name_slug>[\w\-]+)/edit/$', views.edit_band_profile, name='edit_band_profile'),
               )