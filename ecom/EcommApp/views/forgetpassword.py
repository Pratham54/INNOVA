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
                <div style="text-align: center; padding: 30px; border: 1px solid #ddd; border-radius: 10px; font-family: Arial, sans-serif;">
                    <div style="margin-bottom: 30px;">
                        <h1 style="font-family: 'Montserrat', sans-serif; font-size: 42px; font-weight: 700; color: #000; margin: 0; position: relative; display: inline-block;">
                            <svg style="width: 24px; height: 24px; position: absolute; left: -30px; top: 50%; transform: translateY(-50%); fill: #e74c3c;" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M23 9l-11-7-11 7v11h22v-11zm-3 9h-4v-4h4v4zm-6-4v4h-4v-4h4zm-6 0v4h-4v-4h4zm14-3l-9-6-9 6h18z"/>
                            </svg>
                            INNOVA
                        </h1>
                    </div>
                    <h2 style="color: #333; font-size: 24px; margin-bottom: 20px;">Hello</h2>
                    <p style="font-size: 16px; color: #555; margin-bottom: 25px;">Here is your OTP for resetting your password:</p>
                    <h1 style="background-color: #f8f9fa; padding: 15px 30px; border-radius: 8px; display: inline-block; font-size: 32px; color: #2c3e50; margin: 0;">{otp}</h1>
                    <p style="color: #777; margin-top: 25px;">This OTP will expire in 10 minutes.</p>
                    <p style="color: #555;">If you didn't request this, please ignore this email.</p>
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
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