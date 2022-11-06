from django.shortcuts import render,redirect
from app.models import *
from django.db import IntegrityError


def showIndex(request):
    return render(request,"index.html")


def save_enquiry(request):
    nm = request.POST.get("p1")
    em = request.POST.get("p2")
    cn = request.POST.get("p3")
    msg = request.POST.get("p4")
    try:
        EnquiryModel(name=nm, email=em, phone=cn, message=msg).save()
        return render(request,"contactus.html",{"data":"Your Enquiry is Submitted Successfully"})
    except IntegrityError:
        return render(request, "index.html", {"error": "Your Enquiry is Already Submitted"})


def why_we(request):
    return render(request,"why_we.html")


def home_page(request):
    return render(request,"home_page.html")


def services(request):
    return render(request,"services.html")


def contactus(request):
    return render(request, "contactus.html")


def accounting_services(request):
    return render(request,"accounting_services.html")


def taxation_services(request):
    return render(request,"taxation_services.html")


def compliance_services(request):
    return render(request,"compliance_services.html")


def auditing_services(request):
    return render(request,"auditing_services.html")


def career(request):
    return render(request,"career.html")


def save_trainingQuery(request):
    nm = request.POST.get("p1")
    em = request.POST.get("p2")
    pn = request.POST.get("p3")
    qu = request.POST.get("p4")
    dob = request.POST.get("p5")
    exp = request.POST.get("p6")
    dg = request.POST.get("p7")
    rs = request.FILES["p8"]
    try:
        CareerModel(name=nm, email=em, phone=pn, qualification=qu,dob=dob,experience=exp,designation=dg,resume=rs).save()
        return render(request,"career.html",{"data": "Your Query is Submitted Successfully."})
    except IntegrityError:
        return render(request, "career.html", {"error": "Your Query is Already Submitted"})
