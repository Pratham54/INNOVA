from django.shortcuts import render, redirect
from django.views import View
from EcommApp.models.user import UserSignup
from django.contrib import messages
from django.http import HttpResponseRedirect

class UserProfile(View):
    def get(self, request):
        # Check if user is logged in
        if not request.session.get('user_id'):
            messages.error(request, "Please login to access your profile.")
            return redirect('login_page')
            
        updated = request.GET.get("updated", False)
        return render(request, 'userprofile.html', {'updated': updated})

    def post(self, request):
        # Check if user is logged in
        if not request.session.get('user_id'):
            messages.error(request, "Please login to update your profile.")
            return redirect('login_page')

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        profile_pic = request.FILES.get("profile_pic")

        # Get user by ID from session instead of email
        try:
            user = UserSignup.objects.get(id=request.session.get('user_id'))
        except UserSignup.DoesNotExist:
            messages.error(request, "User not found. Please login again.")
            return redirect('login_page')

        # Update user details
        user.full_name = full_name
        user.email = email

        if profile_pic:
            user.profile_pic = profile_pic

        try:
            user.save()

            # Update session data
            request.session['user_full_name'] = full_name
            request.session['user_email'] = email
            if profile_pic:
                request.session['user_profile_pic'] = user.profile_pic.url

            request.session.modified = True
            request.session.save()

            messages.success(request, "Your profile has been updated successfully.")
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f"Error updating profile: {str(e)}")
            return redirect('userprofile')
