from django.db import models
from django.contrib.auth.models import User

class HotelTypes:
    HOME_STAY = 'home_stay'
    VILLA = 'villa'
    LODGE = 'lodge'
    FIVE_STAR = 'five_star'
    REGULAR = 'regular'

    CHOICES = ((HOME_STAY, 'Home Stay'), (VILLA, 'Villa'), (LODGE, 'Lodge'), (FIVE_STAR, 'Five Star'),
               (REGULAR, 'Regular'))
    
class BookingStatuses:
    ACTIVE = 'active'
    CANCELLED = 'cancelled'
    ON_HOLD = 'on_hold'

    CHOICES = ((ACTIVE, 'Active'), (CANCELLED, 'Cancelled'), (ON_HOLD, 'On Hold'))

class ContactPerson(User):
    phone = models.CharField(max_length=20, null=False)
    signedup_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.get_full_name(),
            "phone": self.phone,
            "email": self.email,
            "signedup_on": str(self.signedup_on)
        }


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField()
    checkin_time = models.DateTimeField(null=False)
    checkout_time = models.DateTimeField(null=False)
    hotel_type = models.CharField(choices=HotelTypes.CHOICES, default=HotelTypes.REGULAR, max_length=255)
    contact_person = models.ForeignKey('hotels.ContactPerson', on_delete=models.CASCADE)
    n_rooms = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "checkin_time": str(self.checkin_time),
            "checkout_time": str(self.checkout_time),
            "hotel_type": self.hotel_type,
            "contact_person": self.contact_person.to_json() if self.contact_person else {},
            "n_rooms": self.n_rooms
        }

class Room(models.Model):
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.PROTECT)
    occupancy = models.IntegerField()
    charges = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def to_json(self):
        return {
            "id": self.id,
            "hotel": self.hotel_id,
            "occupancy": self.occupancy,
            "charges": self.charges,
            "is_verified": self.is_verified
        }

class Amenities(models.Model):
    room = models.ForeignKey('hotels.Room', on_delete=models.CASCADE)
    has_wifi = models.BooleanField(default=False)
    has_ac = models.BooleanField(default=False)
    has_hot_water = models.BooleanField(default=False)
    has_locker = models.BooleanField(default=False)
    has_free_breakfast = models.BooleanField(default=False)


class Booking(models.Model):
    room = models.ForeignKey('hotels.Room', on_delete=models.CASCADE)
    customer = models.ForeignKey('hotels.Customer', on_delete=models.CASCADE)
    booked_on = models.DateTimeField(null=False)
    status = models.CharField(choices=BookingStatuses.CHOICES, default=BookingStatuses.ACTIVE, null=False, max_length=255)
    amount_paid = models.IntegerField()
    start_date = models.DateTimeField(null=False)
    end_date = models.DateField(null=False)
    invoice = models.CharField(null=True, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "id": self.id,
            "room": self.room_id,
            "customer": self.customer_id,
            "booked_on": str(self.booked_on),
            "amount_paid": self.amount_paid,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "invoice": self.invoice
        }
        
