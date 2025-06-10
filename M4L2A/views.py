from django.shortcuts import render

from M4L2A.models import Room, Booking

# Create your views here.
def main_page(request):
    rooms = Room.objects.all()
    context = {
        "data": "hello from Django",
        'room_list': rooms
    }

    return render(request,"M4L2A/room_list.html", context)