from django.contrib import admin
from .models import *
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'room', 'date_in','date_out')
    search_fields = ('name', 'room', 'phone')
    odering = ('-date_in')
admin.site.register(TypeRoom)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Room)