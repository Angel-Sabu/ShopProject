from django.shortcuts import render, redirect
from SHOAPAPP.models import shopDB, productDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from Frontend.models import contactDB
from django.contrib import messages



# Create your views here.
def indexpage(request):
    return render(request, "index.html")


def CategoryPage(request):
    return render(request, "addcategory.html")


def savedata1(request):
    if request.method == "POST":
        n = request.POST.get('CategoryName')
        d = request.POST.get('Description')
        i = request.FILES['CategoryImage']
        obj = shopDB(CategoryName=n, Description=d, CategoryImage=i)
        obj.save()
        messages.success(request, "Category Saved SuccessFully...!!")
        return redirect(CategoryPage)


def Categorydisplaypage(request):
    data = shopDB.objects.all()
    return render(request, "categorydisplay.html", {'data': data})


def categoryeditpage(request, dataid):
    cat = shopDB.objects.get(id=dataid)
    return render(request, "categoryedit.html", {'cat': cat})


def updatecategory(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('CategoryName')
        des = request.POST.get('Description')
        try:
            img = request.FILES['CategoryImage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = shopDB.objects.get(id=dataid).CategoryImage
        shopDB.objects.filter(id=dataid).update(CategoryName=cn, Description=des, CategoryImage=file)
        messages.success(request, "Category Edited SuccessFully...!!")
        return redirect(Categorydisplaypage)


def deletecategory(request, dataid):
    cat = shopDB.objects.filter(id=dataid)
    cat.delete()
    return redirect(Categorydisplaypage)


# products Details

def Productspage(request):
    category = shopDB.objects.all()
    return render(request, "addproducts.html", context={"category": category})


def productsavedata(request):
    if request.method == "POST":
        ca = request.POST.get('CategoryName')
        po = request.POST.get('ProductName')
        de = request.POST.get('Description')
        pr = request.POST.get('Price')
        pi = request.FILES['ProductImage']
        obj = productDB(CategoryName=ca, ProductName=po, Description=de, Price=pr, ProductImage=pi)
        obj.save()
        messages.success(request, "Product Saved SuccessFully...!!")
        return redirect(Productspage)


def Productsdisplaypage(request):
    data = productDB.objects.all()
    return render(request, "productsdisplay.html", {'data': data})


def producteditpage(request, dataid):
    prdt = productDB.objects.get(id=dataid)
    category = shopDB.objects.all()
    return render(request, "productedit.html", {'prdt': prdt, 'category': category})


def updateproduct(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('CategoryName')
        pn = request.POST.get('ProductName')
        des = request.POST.get('Description')
        pr = request.POST.get('Price')
        try:
            img = request.FILES['ProductImage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productDB.objects.get(id=dataid).ProductImage
        productDB.objects.filter(id=dataid).update(CategoryName=cn, ProductName=pn, Description=des, Price=pr,
                                                   ProductImage=file)
        messages.success(request, "Product Edited SuccessFully...!!")
        return redirect(Productsdisplaypage)


def deleteproduct(request, dataid):
    prdt = productDB.objects.filter(id=dataid)
    prdt.delete()
    return redirect(Productsdisplaypage)


def loginpages(request):
    return render(request, "loginpage.html")


def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request, "Login SuccessFully...!!")
                return redirect(indexpage)

            else:
                return redirect(loginpages)
        else:
            return redirect(loginpages)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)


def contactus(request):
    data = contactDB.objects.all()
    return render("view_contactus.html", {"data": data})
