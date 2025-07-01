from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from M4L2A.forms import BookingForm
from M4L2A.models import Room, Booking


# Create your views here.
def main_page(request):
    rooms = Room.objects.all()
    context = {
        "data": "hello from Django",
        'room_list': rooms
    }

    return render(request,"M4L2A/room_list.html", context)

@login_required
def booking_page(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            return redirect("main")

    context = {
        'room' : room,
        'form' : form
    }

    return render(request, 'M4L2A/booking_page.html', context)