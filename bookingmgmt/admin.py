from django.contrib import admin
from bookingmgmt.models import Room_Type, Room, Reservation, Guest, Charge

admin.site.register(Room_Type)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Charge)