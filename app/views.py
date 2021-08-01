from django.shortcuts import render

from app.models import Product, Checkout

from django.views.generic import DetailView
# Create your views here.


def homeView(request):
    return render(request, "home.html")


def readDetails(request):
    all_products = Product.objects.all()

    if request.method == "POST":
        itemName = request.POST.get('search')  # itemName="shirt"

        if itemName != '' and itemName is not None:
            all_products = all_products.filter(name__exact=itemName)

    context = {
        'all_products': all_products
    }
    return render(request, "home.html", context)


class readOneData(DetailView):
    model = Product


def checkout(request):
    return render(request, "checkout.html")


def formView(request):
    if request.method == "POST":
        myfname = request.POST.get("fname")
        mylname = request.POST.get("lname")
        myemail = request.POST.get("email")
        myphoneno = request.POST.get("phoneno")
        mycity = request.POST.get("city")
        mypincode = request.POST.get("pincode")
        myaddress = request.POST.get("address")
        myprice = request.POST.get("price")

        c = Checkout(firstName=myfname, lastName=mylname, emailId=myemail, phoneNo=myphoneno,
                     city=mycity, pincode=mypincode, address=myaddress, price=myprice)

        c.save()

    return render(request, "form.html")
