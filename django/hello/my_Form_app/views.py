from django.shortcuts import render, HttpResponse
from datetime import datetime
from my_Form_app.models import Log
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")
def about(request):
    return HttpResponse("this is aboutpage")

def form(request):
    return HttpResponse("this is formpage")

def log(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        #password = request.POST.get('password')
        feedback = request.POST.get('feedback')
        log = Log(name=name, email=email, phone=phone, feedback=feedback, date=datetime.today())
        log.save()
        messages.success(request, "your massage has been sent!!")
    
    return render(request, 'log_in.html') 

#def test(request):
   # return HttpResponse("this is formpage")

