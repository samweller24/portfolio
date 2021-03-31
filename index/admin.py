from django.contrib import admin
from .models import about
from .models import slider,client,project

# Register your models here.

admin.site.register(about)
admin.site.register(slider)
admin.site.register(client)
admin.site.register(project)