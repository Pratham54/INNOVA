from django.views import View
from EcommApp.models.user import UserSignup
from django.contrib import messages  # Import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.conf import settings

class LoginPage(View):
    return_Url = None

    def get(self, request):
        LoginPage.return_Url = request.GET.get('return_Url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserSignup.get_customer_by_email(email)
        
        if user:
            # Check password
            if check_password(password, user.password):
                # Setting session data for user info
                request.session['user_id'] = user.id
                request.session['user_full_name'] = user.full_name
                request.session['user_email'] = user.email
                request.session['user_profile_pic'] = (
                    f"{settings.MEDIA_URL}{user.profile_pic}"
                    if user.profile_pic else None
                )

                # Success Message
                messages.success(request, "Login successful! Welcome back.")
                print(request.session)
                return redirect('home')  # Redirect to homepage after login
            else:
                messages.error(request, "Invalid password!")  # Error Message
        else:
            messages.error(request, "Invalid email!")  # Error Message

        print(password, email)
        print("Failed The File")
        return render(request, 'login.html')
    
def logout(request):
    # First, flush the session which properly cleans up all session data
    request.session.flush()
    # Then clear any remaining session data
    request.session.clear()
    messages.info(request, "You have successfully logged out.")
    # Force a new session to be created for the next login
    request.session.create()
    return redirect('login_page')
