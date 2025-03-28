from django.views import View
from django.shortcuts import render

class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')