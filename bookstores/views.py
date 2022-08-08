from email.mime import image
from django.shortcuts import redirect,render
from bookstores.forms import loginform,signup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from user.models import userdetail,books

def home(request):
    fm=loginform()
    if request.method=="POST":
        fm=loginform(request.POST)
        if fm.is_valid():
            global username
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']

            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("/mystore")
            else:
                messages.error(request,"Username or password incorrect")
                
    return render(request,"logintemplate.html",{"form":fm})


def register(request):
    fm=signup()
    if request.method=="POST":

        fm=signup(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            username=fm.cleaned_data['username']
            email=fm.cleaned_data['email']
            store=fm.cleaned_data['store']
            password=fm.cleaned_data['password']

            newuser = User.objects.create_user(username,email,password)
            newuser.save()
            userdetail(username=username,name=name,store=store).save()
            
            return redirect("/")
            
    return render(request,"registertemplate.html",{"form":fm})

def mystore(request):
    boo=books.objects.filter(username=username)
    global usernam
    usernam=userdetail.objects.get(username=username)
    if request.method=="POST":
        searchmybook=request.POST.get('searchmybook')
        boo=books.objects.filter(username=username,book__icontains=searchmybook)
    return render(request,"mystore.html",{"books":boo,"user":usernam.store})


def update(request,bookid):
    bo=books.objects.get(id=bookid)
    store=userdetail.objects.get(username=username)
    if request.method=="POST":
        bookss=request.POST.get('book')
        price=request.POST.get('price')
        author=request.POST.get('author')
        counts=request.POST.get('counts')
        books(id=bookid,book=bookss,price=price,author=author,counts=counts,username=username,store=store.store).save()
        
        return redirect("/mystore")
    return render(request,"update.html",{"books":bo,"user":usernam.store})

def remove(request,bookid):
    books(id=bookid).delete()
    return redirect("/mystore")

def addbook(request):
    store=userdetail.objects.get(username=username)
    if request.method=="POST":
        book=request.POST.get('book')
        price=request.POST.get('price')
        author=request.POST.get('author')
        counts=request.POST.get('counts')

        books(book=book,price=price,author=author,counts=counts,username=username,store=store.store).save()
        return redirect("/mystore")

    return render(request,"addbook.html",{"user":usernam.store})
        
def storelist(request):
    stores=userdetail.objects.all()
    if request.method=="POST":
        searchstore=request.POST.get('searchstore')
        stores=userdetail.objects.filter(store__icontains=searchstore)
    return render(request,"home.html",{"store":stores,"user":usernam.store})

def storeinfo(request,storeid):

    st=books.objects.filter(store=storeid)
    if request.method=="POST":
        searchbook=request.POST.get('searchbook')
        st=books.objects.filter(book__icontains=searchbook)
    return render(request,"storeinfo.html",{"st":st,"user":usernam.store,"store":storeid})

def about(request):
    return render(request,"about.html",{"user":usernam.store})

def contact(request):
    return render(request,"contact.html",{"user":usernam.store})


def logoutt(request):
    logout(request)
    return redirect('/')










