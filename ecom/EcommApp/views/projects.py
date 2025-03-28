from django.views import View
from django.shortcuts import render,redirect
from EcommApp.models.projects import Projects

class ProjectsPage(View):
    def get(self, request):
        all_projects=Projects.objects.all()
        print("allProjects:",all_projects)
        return render(request, 'projects.html',{"all_projects":all_projects})
    
    def post(request):
        name=request.POST.get("name")
        
        image=request.FILES.get("image")
        
        if name and image:
           Projects.objects.create(name=name,image=image)
            
        return redirect('projects')