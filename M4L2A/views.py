from django.shortcuts import render, get_object_or_404

from M4L2A.models import Room, Booking

# Create your views here.
def main_page(request):
    rooms = Room.objects.all()
    context = {
        "data": "hello from Django",
        'room_list': rooms
    }

    return render(request,"M4L2A/room_list.html", context)

def booking_page(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    context = {
        'room' : room
    }

    return render(request, 'M4L2A/booking_page.html', context)