from django.shortcuts import render, HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return HttpResponse("Hello world from Django, Gunicorn, Docker and NGINX")

def test(request):
    return render( request, 'test.html')