from django.contrib import admin

from .models import Task, Plan

admin.site.site_header = "Tasks Admin"
admin.site.site_title = "Tasks Admin Area"
admin.site.index_title = "Welcome to Tasks Admin"

# have choices within admin screen 

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['task_title']}), 
        (None, {'fields': ['task_description']}), 
        (None, {'fields': ['completed', 'important', 'archive']}), 
        (None, {'fields': ['author']}), 
        (None, {'fields': ['parent_plan']}), 
        ('Date Information', 
            {
                'fields': ['creation_date', 'updated_date', 'due_date'], 
                'classes':['collapse'],
            }
        )    
    ]

class PlanAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['plan_title']}), 
        (None, {'fields': ['plan_description']}), 
        (None, {'fields': ['completed', 'important', 'archive']}), 
        (None, {'fields': ['author']}), 
        ('Date Information', 
            {
                'fields': ['creation_date', 'updated_date', 'due_date'], 
                'classes':['collapse'],
            }
        )    
    ]

admin.site.register(Plan, PlanAdmin)
admin.site.register(Task, TaskAdmin)