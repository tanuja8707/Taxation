"""Accountancy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Accountancy import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="main"),
    path('save_enquiry/',views.save_enquiry,name="save_enquiry"),
    path('why_we/',views.why_we,name="why_we"),
    path('home_page/',views.home_page,name="home_page"),
    path('services/',views.services,name="services"),
    path('contactus/',views.contactus,name="contactus"),
    path('accounting_services/',views.accounting_services,name="accounting_services"),
    path('taxation_services/',views.taxation_services,name="taxation_services"),
    path('compliance_services/',views.compliance_services,name="compliance_services"),
    path('auditing_services/',views.auditing_services,name="auditing_services"),
    path('career/',views.career,name="career"),
    path('save_trainingQuery/',views.save_trainingQuery,name="save_trainingQuery"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)