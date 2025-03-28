from django.views import View
from django.shortcuts import render,redirect
from EcommApp.models.services import Services

class ServicesPage(View):
    def get(self, request):
        all_services=Services.objects.all()
        print("allServices:",all_services)
        return render(request, 'services.html',{"all_services":all_services})
    
    def post(request):
        name=request.POST.get("name")
        content=request.POST.get("content")
        image=request.FILES.get("image")
        
        if name and content and image:
            Services.objects.create(name=name,content=content,image=image)
            
        return redirect('services')
        
        

