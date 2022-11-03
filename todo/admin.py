from django.contrib import admin
from .models import todo, notes
# Register your models here.
@admin.register(todo)

class todomodel(admin.ModelAdmin):
   list_display = [f.name for f in todo._meta.fields]