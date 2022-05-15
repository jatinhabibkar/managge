from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('student/<int:studentId>',views.searchByStudentId,name='student'),

]