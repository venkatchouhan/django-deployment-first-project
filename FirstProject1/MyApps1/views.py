from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def display(request):
    return HttpResponse('<center><h1> hello user welcome to the django first project</h1><hr/>')


def f1(request):
    return HttpResponse("<center><h1 style ='color:red';> Good morning user have a nice day ...!!!!</h1><hr/>");
def f2(request):                     
    return HttpResponse("<center><h2 style ='color:orange';> Good afternnon user i hope u doing good ....</h2><hr/>");
def f3(request):
    return HttpResponse("<center><h3 style ='color:skyblue';> Good night user have a great day</h3><hr/>");


def f11(request):
    return HttpResponse("<center><h1 style ='color:red';> Good morning user have a nice day ...!!!!</h1><hr/>")


from django.http import HttpResponse;
import datetime;
def f22(request):
	time = datetime.datetime.now();
	msg = "<h2 style='color:Green;'>Hello User..!!<br /><br />Server Date & Time :: "+str(time)+"</h2><hr/>"
	return HttpResponse(msg);
