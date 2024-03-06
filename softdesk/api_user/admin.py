from django.contrib import admin
from api_project.models import Project, Comment, Issue, Contributor

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'project')

