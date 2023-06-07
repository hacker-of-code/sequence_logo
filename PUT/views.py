from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    message = ""
    if request.method == "POST":
        sequence = request.POST.get("sequence", "")
        request.session["sequence"] = sequence

        return redirect("/GET/get_sequence_logo/")
    context = {"message": message}
    return render(request, "i.html", context)