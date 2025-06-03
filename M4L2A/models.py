from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TypeRoom(models.Model):
    name = models.CharField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Тип кімнати:{self.name}"

class Room(models.Model):
    type_room = models.ForeignKey(TypeRoom, on_delete=models.CASCADE, related_name="rooms")
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="Rooms", null=True)
    description = models.TextField(null=True, blank=True)
    places = models.IntegerField(default=1)
    rooms = models.IntegerField(default=1)

    def __str__(self):
        return f"Кімната:{self.name}, ціна:{self.price}."

    #class Meta():
        #verbose_name =

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    c_time = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'Бронювання:{self.room}, Дата заїзду:{self.date_in}, Дата виїзду:{self.date_out}'
