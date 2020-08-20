from django.contrib import admin

from .models import Task

admin.site.site_header = "Tasks Admin"
admin.site.site_title = "Tasks Admin Area"
admin.site.index_title = "Welcome to Tasks Admin"

# have choices within admin screen 

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['task_text']}), 
        ('Date Information', 
            {
                'fields': ['creation_date'], 
                'classes':['collapse'],
            }
        )    
    ]

admin.site.register(Task, TaskAdmin)