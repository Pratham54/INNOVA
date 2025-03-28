from django.urls import path,include
from django.conf.urls.static import static
from EcommApp.views.index import Index
from EcommApp.views.Signup import SignupPage
from EcommApp.views.login import LoginPage,logout
from EcommApp.views.about import AboutPage
from EcommApp.views.services import ServicesPage
from EcommApp.views.projects import ProjectsPage
from EcommApp.views.testimonials import TestimonialsPage

from EcommApp.views.home import HomePage
from django.conf import settings
from EcommApp.views.forgetpassword import ForgetPassword
from EcommApp.views.resetpassword import ResetPassword
from EcommApp.views.verifyotp import VeryfyOTP
from EcommApp.views.userProfile import UserProfile
from EcommApp.views.contact import Contact

urlpatterns = [
    path("",Index,name='home'),
    path("signup",SignupPage.as_view(),name='signup'),
    path("login",LoginPage.as_view(),name='login_page'),
    path("about",AboutPage.as_view(),name='about'),
    path("services",ServicesPage.as_view(),name='services'),
    path("projects",ProjectsPage.as_view(),name='projects'),
    path("testimonials",TestimonialsPage.as_view(),name='testimonials'),
    path("contact",Contact,name='contact'),
    path("home",HomePage.as_view(),name='home'),
    path("logout",logout,name='logout'),
    path('forget-password', ForgetPassword.as_view(), name='forgetpassword'),
    path("reset-password", ResetPassword.as_view(), name="resetpassword"),
    path("verify-otp", VeryfyOTP.as_view(), name="verifyotp"), 
   path('userprofile/', UserProfile.as_view(), name='userprofile'),
    ]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


