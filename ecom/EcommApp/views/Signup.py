from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages
from EcommApp.models.user import UserSignup
from django.contrib.auth.hashers import make_password

class SignupPage(View):
    def get(self, request):
        return render(request, 'Signup.html')

    def post(self, request):
        postData = request.POST
        full_name = postData.get("full_name", "").strip()
        email = postData.get("email", "").strip()
        password = postData.get("password")
        confirmpassword = postData.get("confirmpassword")
        profile_pic = request.FILES.get("profile_pic")

        value = {
            "full_name": full_name,
            "email": email,
            "password": password
        }

        error_message = None
        user = UserSignup(
            full_name=full_name,
            email=email,
            password=password,
            profile_pic=profile_pic
        )

        error_message = self.validateUser(user, confirmpassword)

        if not error_message:
            user.password = make_password(user.password)
            user.save()
            messages.success(request, "Signup successful! Please login now.")
            return redirect('/login')
        else:
            messages.error(request, error_message)
            data = {
                'values': value
            }
            return render(request, 'Signup.html', data)

    def validateUser(self, user, confirmpassword):
        error_message = None
        if not user.full_name:
            error_message = "Full name is required!"
        elif len(user.full_name) < 4:
            error_message = "Full name must be 4 characters long or more."
        elif len(user.email) < 6:
            error_message = "Email must be 6 characters long."
        elif not user.password:
            error_message = "Password is required."
        elif len(user.password) < 6:
            error_message = "Password must be 6 characters long."
        elif user.password != confirmpassword:
            error_message = "Password and confirm password do not match."
        elif user.isExists():
            error_message = "Email already exists."
        return error_message
