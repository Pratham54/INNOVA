from django.views import View
from django.shortcuts import render

class TestimonialsPage(View):
    def get(self, request):
        return render(request, 'testimonials.html')