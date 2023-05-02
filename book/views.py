from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def name(request):   
    return HttpResponse("hello")

def contact(request):       #load data 
 return render(request,"book/contact.html")

def view_contact(request):  # selection
   obj=Contact.objects.all()
   return render(request,"book/view_contact.html",{"res":obj})


def Edit_contact(request): # find data
   obj=Contact.objects.get(pk=request.GET["q"])
   return render(request,"book/Edit_contact",{"res":obj})


def edit(request):            
    e=request.POST["txtemail"]
    m=request.POST["txtmobile"]
    msg=request.POST["txtmsg"]
    s = Contact.objects.get(pk=request.POST["txtid"])
    s.emailid=e
    s.mobile=m
    s.message=msg
    s.save()
    return redirect('view_contact')

def Delete_contact(request):    # code to find record for delete operation
    s = Contact.objects.get(pk=request.GET["q"])
    s.delete()
    return redirect('view_contact')


def contact_code(request):        #code to insert record from database
    e=request.POST["txtemail"]
    m=request.POST["txtmobile"]
    msg=request.POST["txtmsg"]
    obj = Contact(emailid=e,mobile=m,message=msg)
    obj.save()
    return redirect('view_contact')
   # return render(request,"scsapp/contact.html",{'res':'data submitted successfully'})