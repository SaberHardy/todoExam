from django.contrib import admin

# Register your models here.
from .models import Task,Borrowed

admin.site.register(Borrowed)
admin.site.register(Task)