from django.shortcuts import render, redirect
from SHOAPAPP.models import shopDB, productDB
from Frontend.models import contactDB, registerDB, Cartdb


# Create your views here.

def homepage(request):
    cat = shopDB.objects.all()
    return render(request, "Home.html", {'cat': cat})


def productpage(request):
    pro = productDB.objects.all()
    return render(request, "Product.html", {'pro': pro})


def singleproductpage(request, proid):
    data = productDB.objects.get(id=proid)
    return render(request, "singleproduct.html", {'data': data})


def filter_prdt_pg(request, cat_name):
    data = productDB.objects.filter(CategoryName=cat_name)
    return render(request, "filterpage.html", {'data': data})


def contactpage(request):
    return render(request, "contact.html")


def aboutpage(request):
    return render(request, "about.html")


def servicepage(request):
    return render(request, "services.html")


def savedata(request):
    if request.method == "POST":
        f = request.POST.get('FirstName')
        l = request.POST.get('LastName')
        e = request.POST.get('Email')
        a = request.POST.get('Address')
        c = request.POST.get('City')
        co = request.POST.get('Country')
        m = request.POST.get('Mobile')
        obj = contactDB(FirstName=f, LastName=l, Email=e, Address=a, City=c, Country=co, Mobile=m)
        obj.save()
        return redirect(contactpage)


def registerpage(request):
    return render(request, "register.html")


def registersave(request):
    if request.method == "POST":
        n = request.POST.get('Name')
        m = request.POST.get('Mobile')
        e = request.POST.get('Email')
        u = request.POST.get('Username')
        r = request.POST.get('RegPassword')
        obj = registerDB(Name=n, Mobile=m, Email=e, Username=u, RegPassword=r)
        obj.save()
        return redirect(registerpage)


def loginpage(request):
    return render(request, "register.html")


def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('Username')
        pwd = request.POST.get('loginpassword')
        if registerDB.objects.filter(Username=un, RegPassword=pwd).exists():
            request.session['Username'] = un
            request.session['RegPassword'] = pwd
            return redirect(homepage)
        else:
            return redirect(registerpage)

    return redirect(registerpage)


def logout(request):
    del request.session['Username']
    del request.session['RegPassword']
    return redirect(loginpage)


def cartpage(request):
    data = Cartdb.objects.filter(UserName=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request, "cart.html", {'data': data, 'total_price': total_price})


def savecart(request):
    if request.method == "POST":
        u = request.POST.get('UserName')
        p = request.POST.get('ProductName')
        d = request.POST.get('Description')
        q = request.POST.get('Quantity')
        t = request.POST.get('TotalPrice')
        obj = Cartdb(UserName=u, ProductName=p, Description=d, Quantity=q, TotalPrice=t)
        obj.save()
        return redirect(cartpage)


def deletecart(request, dataid):
    cart = Cartdb.objects.filter(id=dataid)
    cart.delete()
    return redirect(cartpage)
