from datetime import datetime
from pyclbr import Function
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import ContactusForm,SignUpForm,BookingForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Booking, Contact
from . import forms,models
from django.contrib.auth.models import User
# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return render(request,'index.html',{'name':request.user})
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully !!')
            return HttpResponseRedirect('/login/')
    else:
        fm=SignUpForm()
    return render(request,'singup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    if user.is_superuser:
                        messages.success(request,'Logged in successfully !!')
                        return HttpResponseRedirect("/admin_dashboard")
                    if user.is_staff:
                        messages.success(request,'Logged in successfully !!')
                        return HttpResponseRedirect('/home/')
        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')
def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='login')
def menu(request):
    return render(request,'menu.html')
@login_required(login_url='login')
def event(request):
    return render(request,'event.html')

def about(request):
    return render(request,'about.html')

def aboutus(request):
    return render(request,'about1.html')
@login_required(login_url='login')
def service(request):
    return render(request,'services.html')
    

def contact(request):
    fm=ContactusForm()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        print("Success")
        messages.success(request,'Your message has been sent!')
        return render(request,'dashboard.html')
    return render(request,'contact.html',{'form':fm})  
@login_required(login_url='login')
def booking(request):
    b=models.User.objects.filter(id=request.user.id).values('id')
    bb=models.User.objects.get(id=request.user.id)
    print(bb)
    booking=BookingForm()
    if request.method=='POST':
        f_name = request.POST.get('Event_Name')
        f_date = request.POST.get('Date')
        phone=request.POST.get('Number')
        day=request.POST.get('Day')
        venue=request.POST.get('Venue')
        guest=request.POST.get('Guest')
        Book = Booking(user_id=b,f_name=f_name, date=f_date,number=phone,venue=venue,day=day,guest=guest)
        Book.save()
        messages.success(request,'Your booking has been sent wait some time it will be approved!')
        return redirect('/bookingstatus')
    return render(request,'booking.html',{'form':booking,'data':bb})

@login_required(login_url='login')
def booking_status(request):
    booking=models.User.objects.get(id=request.user.id)
    data=models.Booking.objects.all().filter(user=booking)
    return render(request,'bookingstatus.html',{'booking':booking,'data':data})

@login_required(login_url='login')
def delete_booking(request,pk):
    d=Booking.objects.get(id=pk)
    print(d)
    d.delete()
    return redirect('/bookingstatus')

# ---------------------Admin----------------------------
@login_required(login_url='login')
def admin_dashboard(request):
    dic={
        'total_customer':User.objects.all().filter(is_staff=False).count(),
        'x':User.objects.all().filter(is_staff=True).count(),
        'y':Contact.objects.count()
        }
    return render(request,'admin/admin_dashboard.html',context=dic)
@login_required(login_url='login')
def customer_view(request):
    x=User.objects.all().filter(is_staff=False)
    # print(x)
    return render(request,'admin/customer_view.html',{'x':x})

@login_required(login_url='login')
def delete_customer_view(request,pk):
    x=User.objects.get(id=pk)
    x.delete()
    return HttpResponseRedirect('/customer_view')

d

@login_required(login_url='login')
def delete_contact_list(request,pk):
    question=Contact.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/contactlist')

@login_required(login_url='login')
def admin_menu(request):
    return render(request,'admin/menu.html')

@login_required(login_url='login')
def admin_event(request):
    return render(request,'admin/event.html')

@login_required(login_url='login')
def view_booking(request):
    booking=models.Booking.objects.all()
    return render(request,'admin/booking.html',{'data':booking})

@login_required(login_url='login')
def approve_request_view(request,pk):
    booking = models.Booking.objects.get(id=pk)
    booking.status='Approved'
    booking.save()
    return redirect('/view_booking')

@login_required(login_url='login')
def disapprove_request_view(request,pk):
    booking = models.Booking.objects.get(id=pk)
    booking.status='Disapproved'
    booking.save()
    return redirect('/view_booking')
