from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# request -> respinse
# request handler
'''
def say_hello(request):
    # return HttpResponse("Hello World!")
    return render(request, 'hello.html', {'name': 'Owen'})
'''

# def index(request):
#     message = ""
#     if request.method == "POST":
#         print(1)
#         if request.POST.get("password","") == "123":
#             return redirect("/PUT/put_sequence/")
#         else:
#             message = "Incorrect password"
#     context = {"message": message}
#     print(2)
#     return render(request, "i.html", context)

def index(request):
    message = ""
    if request.method == "POST":
        sequence = request.POST.get("sequence", "")
        request.session["sequence"] = sequence

        return redirect("/GET/get_sequence_logo/")
    context = {"message": message}
    return render(request, "i.html", context)

