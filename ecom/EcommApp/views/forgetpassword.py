from django.shortcuts import render, redirect
from django.views import View
from EcommApp.models.user import UserSignup
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.utils.html import format_html


otp_storage = {}

class ForgetPassword(View):
    def get(self, request):
        return render(request, 'forgetpassword.html')
    
    def post(self, request):
        email = request.POST.get('email')

        # Check if email exists in the database
        user = UserSignup.objects.filter(email=email).first()

        if user:
            otp = random.randint(10000, 999999)
            otp_storage[email] = otp
            print(f"OTP stored for {email}: {otp}")

            request.session['otp'] = otp
            request.session['email'] = email
            request.session.save()

            subject = 'Your OTP for Password Reset'
            from_email = 'your-email@example.com'  # Replace with your email
            to_email = [email]
            # HTML Email Content
            html_content = format_html(f"""
                <div style="text-align: center; padding: 20px; border: 1px solid #ddd; border-radius: 10px; font-family: Arial, sans-serif;">
                    <h1 style="font-family: 'Poppins', sans-serif; font-weight: 700; color: #000;">INNOVA</h1>
                    <h2 style="color: #333;">Hello</h2>
                    <p style="font-size: 16px; color: #555;">Here is your OTP for resetting your password:</p>
                    <h1 style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; display: inline-block;">{otp}</h1>
                    <p style="color: #777;">This OTP will expire in 10 minutes.</p>
                    <p>If you didn't request this, please ignore this email.</p>
                    <hr style="margin-top: 20px;">
                    <p style="font-size: 12px; color: #999;">© 2024 Innova. All rights reserved.</p>
                </div>
            """)
                        # Send Email
            email_message = EmailMultiAlternatives(subject, '', from_email, to_email)
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()

            messages.success(request, "An OTP has been sent to your email address.")
            return redirect('/verify-otp')
        else:
            messages.error(request, "Email does not exist.")
            return render(request, 'forgetpassword.html')