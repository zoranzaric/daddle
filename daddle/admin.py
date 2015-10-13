from django.contrib import admin

from .models import Event, Pledge, Mission

admin.site.register(Event)

admin.site.register(Pledge)

admin.site.register(Mission)
