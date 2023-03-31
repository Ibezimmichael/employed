from django.contrib import admin
from .models import Employee, Department
# Register your models here.
admin.site.register(Employee)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}