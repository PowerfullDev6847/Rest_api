from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Customer(models.Model):
    frist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=12)
    age = models.PositiveIntegerField(max_length=11)
    contact =PhoneNumberField(unique=True)
    email = models.EmailField(max_length=255)

    def __str__(self) :
        return f"{self.frist_name} {self.last_name}"
    class Meta:
        db_table="Customer"


class Ticket(models.Model):
    ticket_num = models.PositiveIntegerField(max_length=20)
    date_avail = models.DateField()
    date_flight = models.DateField()
    time_deport = models.DateTimeField()
    time_land = models.DateTimeField()
    description = models.TextField(null=True, blank=True)

class Reservation(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_res = models.DateTimeField(auto_now_add=True)
    date_accom = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.user = kwargs.pop('users', None)
            super(Reservation, self). save(*args, **kwargs)
