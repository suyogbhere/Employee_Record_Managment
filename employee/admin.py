from django.contrib import admin
from employee.models import Employee_Detail,Employee_Education,Employee_Experience

# Register your models here.

# class Admin_Employee_Detail(admin.ModelAdmin):
#     list_display = ['user','empcode','empdept','designation','contact','gender','joining_date']

admin.site.register(Employee_Detail)

admin.site.register(Employee_Education)

admin.site.register(Employee_Experience)
