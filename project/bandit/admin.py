from django.contrib import admin
from bandit.models import Profile, Band, Venue, Event, Request, Image

class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('date',)}

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Band)
admin.site.register(Venue)
admin.site.register(Event, EventAdmin)
admin.site.register(Request)
admin.site.register(Image)