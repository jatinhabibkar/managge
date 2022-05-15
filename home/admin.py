from django.contrib import admin
from .models import School,Book,Student
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display =('id','name','is_active')
    list_display_links = ('id','name')
    list_editable = ['is_active']
    list_per_page = 25

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    list_display_links = ('id','name')
    list_editable = ['is_active']
    list_per_page = 25

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','gender','school','book')
    list_display_links = ('id','first_name')
    list_per_page = 25

admin.site.register(Student, StudentAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(School, SchoolAdmin)
