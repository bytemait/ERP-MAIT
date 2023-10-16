from django.contrib import admin

from .models.user_model import User
from .models.student_model import Student
from .models.employee_model import Employee

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'name']


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)