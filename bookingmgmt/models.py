from django.db import models

from django.utils import timezone

class Room_Type(models.Model):
    max_guests = models.IntegerField(default=0)
    total_rooms = models.IntegerField(default=0)
    room_price = models.IntegerField(default=0)

class Room(models.Model):
    room_no = models.CharField(max_length=5)
    room_type = models.ForeignKey(Room_Type, on_delete = models.CASCADE)

    def __str__(self):
        return self.room_no

class Guest(models.Model):
    guest_fname = models.CharField(max_length=30)
    guest_lname = models.CharField(max_length=30)
    guest_phone = models.CharField(max_length=20)
    guest_country = models.CharField(max_length=30)
    guest_email = models.EmailField()

    def __str__(self):
        return self.guest_fname

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    is_cancelled = models.BooleanField(blank=True)
    cancellation_date = models.DateField()

class Charge(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    minibar = models.BooleanField(blank=True)
    room_service = models.BooleanField(blank=True)
    early_checkIn = models.BooleanField(blank=True)