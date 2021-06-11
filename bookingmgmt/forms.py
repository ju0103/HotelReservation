from django import forms
from bookingmgmt.models import Guest, Reservation, Charge

class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        #field = ['room', 'guest', 'arrival_date', 'departure_date', 'is_cancelled', 'cancellation_date']

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'
        #field = ['guest_fname', 'guest_lname', 'guest_phone', 'guest_country', 'guest_email']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = '__all__'
        #field = ['reservation', 'minibar', 'room_service', 'early_checkIn']