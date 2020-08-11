from django.contrib import admin
from .models import Cab, Rider, Location, Trip

# Register your models here.
admin.site.register(Cab)
admin.site.register(Rider)
admin.site.register(Location)
admin.site.register(Trip)
