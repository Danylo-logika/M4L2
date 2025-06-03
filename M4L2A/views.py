from django.shortcuts import render

# Create your views here.
def main_page(request):

    context = {
        "data": "hello from Django"
    }

    return render(request,"index.html", context)