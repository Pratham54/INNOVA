from django.contrib import admin
from .models.user import UserSignup
from .models.contact import Contact
from .models.services import Services
from .models.projects import Projects


admin.site.register(UserSignup)
admin.site.register(Contact)
admin.site.register(Services)
admin.site.register(Projects)