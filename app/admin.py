from django.contrib import admin
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'link')


admin.site.register(Projects, ProjectsAdmin)