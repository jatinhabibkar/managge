from unicodedata import name
from django.contrib import messages
from django.shortcuts import redirect, render

from home.models import Book, School, Student,GENDER_CHOICES

# Create your views here.

def index(request):
    #home page get request
    books = Book.objects.filter(is_active=True)
    schools = School.objects.filter(is_active=True)
    context={
        'books':books,
        'schools':schools,
        'gender':GENDER_CHOICES
    }
    # search query
    if request.method == 'POST':
        try:
            studentId = request.POST['userId'].strip()
            studentName = request.POST['userName'].strip()

            if(studentId == '' and studentName == ''):
                messages.error(request,'plz provide valide search query')
                return redirect('/#search')
            
            if(len(studentId) > 0 and len(studentName) > 0):
                messages.error(request,'plz provide studentid or studentName')
                return redirect('/#search')

            if(studentId != ''):
                studentData = Student.objects.filter(id=int(studentId))
            elif(studentName != ''):
                studentData = Student.objects.filter(first_name__contains=studentName)
            
            if(studentData.exists()):
                context['students']=studentData
                return render(request,'home/index.html',context=context)
            else:
                messages.error(request,'user not found')
                return redirect('/#search')
        except Exception as e:
            messages.error(request,'something went wrong')
            # redirect to search page
            return redirect('/#search')
    
    return render(request,'home/index.html',context=context)

def addstudent(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST.get('last_name')
            
            gender='N'
            if(request.POST.get('gender')):
                gender = request.POST['gender']

            schoolName = request.POST['schoolName']
            book = request.POST['book']
            pages_read_count = request.POST['count']

            student =Student(
                first_name=first_name,
                last_name=last_name,
                email=email,
                school =School.objects.get(id=schoolName),
                gender =gender,
                book = Book.objects.get(id=book),
                pages_read_count = pages_read_count
            )
            student.save()
            messages.success(request, 'Your request has submitted')
            print(email,first_name,last_name,schoolName,gender)
        except Exception as e:
            print(e)
            messages.error(request,'something went wrong')
            return redirect('/#home')

    return redirect('index')


def searchByStudentId(request,studentId):

    studentData = Student.objects.filter(id=int(studentId))

    context={
        'students':studentData,
    }
    if(studentData.exists()):
        return render(request,'home/studentData.html',context=context)
    else:
        messages.error(request,'user not found try name search')
        return redirect('/#search')
    
