from django.contrib import admin
from bandit.models import Profile, Band, Venue, Event, Request, Image

# Register your models here.

admin.site.register(Profile)
admin.site.register(Band)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Request)
admin.site.register(Image)