from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def put_sequence(request):
    return render(request, 'put_sequence.html')