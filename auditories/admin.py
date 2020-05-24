from django.contrib import admin
from .models import User, Room, Reservations


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Reservations)

# Register your models here.
