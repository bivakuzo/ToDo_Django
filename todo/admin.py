from django.contrib import admin
from .models import Task

# Overwriting the admin functionality for Task app
# The class name should be <your_app_name>Admin. 
# Here my app name is Task. So, class name will be TaskAdmin
class TaskAdmin(admin.ModelAdmin):
    # Displaying the items as a list in admin pannel
    list_display = ('task', 'is_completed', 'updated_at')

    # Adding search functionaly in the admin pannel
    search_fields = ('task',)

# Register your models here.
admin.site.register(Task, TaskAdmin)    # Lastly we need to register the class with our app.
