from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from io import BytesIO
from blog.models import Codes
from time import sleep
import base64
import subprocess
import os.path
from django.contrib import messages

from .forms import StudentForm
from blog.models import Students
from .codegenerator import CodeGenerator

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            qr_code = CodeGenerator(form.cleaned_data['student_number'],
                                            form.cleaned_data['student_name'],
                                            form.cleaned_data['student_nickname'],
                                            form.cleaned_data['student_birthdate'],
                                            form.cleaned_data['student_contact'],
                                            form.cleaned_data['student_leader'],
                                            form.cleaned_data['student_contactleader'],
                                            form.cleaned_data['student_network'])
            response = HttpResponse(content_type='image/png')
            qr_code.save(response)            
            return response
    else:
        form = StudentForm()
    return render(request, 'code_home.html', {'form': form})

def generate(request):
    if request.method == 'GET':
        student_level = request.GET.get('student_level')
        student_number = request.GET.get('student_number')
        student_name = request.GET.get('student_name')
        student_nickname = request.GET.get('student_nickname')
        student_birthdate = request.GET.get('student_birthdate')
        student_contact = request.GET.get('student_contact')
        student_leader = request.GET.get('student_leader')
        student_contactleader = request.GET.get('student_contactleader')
        student_network = request.GET.get('student_network')
        qr_code = CodeGenerator(student_level, student_number, student_name, student_nickname, student_birthdate, student_contact, student_leader, student_contactleader, student_network)
        buffered = BytesIO()
        qr_code.save(buffered)
        code_64_encode = base64.b64encode(buffered.getvalue())
        code_instance = Codes.objects.create(
            code_bytes = code_64_encode
        )

        directory = os.path.expanduser('~/Downloads')
        if not os.path.exists(directory + "/codes"):
                os.mkdir(directory + "/codes")
        if student_level == "lifeclass":
            if not os.path.exists(directory + "/codes/lifeclass"):
                os.mkdir(directory + "/codes/lifeclass")
            directory = directory + "/codes/lifeclass"
        if student_level == "sol1":
            if not os.path.exists(directory + "/codes/sol1"):
                os.mkdir(directory + "/codes/sol1")
            directory = directory + "/codes/sol1"
        if student_level == "sol2":
            if not os.path.exists(directory + "/codes/sol2"):
                os.mkdir(directory + "/codes/sol2")
            directory = directory + "/codes/sol2"

        filename = directory + "/" + student_number
        fh = open(''.join([filename, '.png']), "wb")
        fh.write(buffered.getvalue())
        fh.close()
        isfile = False
        delim = True
        fname = ''.join([filename, '.png'])

        return JsonResponse({'code': str(code_64_encode, 'utf-8'), 'id': code_instance.id})

def addstudent(request):
    if request.method == 'GET':
        student_level = request.GET.get('student_level')
        student_number = request.GET.get('student_number')
        student_name = request.GET.get('student_name')
        student_nickname = request.GET.get('student_nickname')
        student_birthdate = request.GET.get('student_birthdate')
        student_contact = request.GET.get('student_contact')
        student_leader = request.GET.get('student_leader')
        student_contactleader = request.GET.get('student_contactleader')
        student_network = request.GET.get('student_network')
        if not Students.objects.filter(student_number = student_number).exists():
            student_instance = Students.objects.create(
                student_level = student_level,
                student_number = student_number,
                student_name = student_name,
                student_nickname = student_nickname,
                student_birthdate = student_birthdate,
                student_contact = student_contact,
                student_leader = student_leader,
                student_contactleader = student_contactleader,
                student_network = student_network
            )
        else:
            messages = "Student " + student_number + " already exists."
            return JsonResponse({'message': messages})
        
        if Students.objects.filter(student_number = student_number).exists():
            messages = "Student " + student_number +" added successfully."
        else:
            messages = "Failed to add student " + student_number
    return JsonResponse({'message': messages})

def editstudent(request):
    if request.method == 'GET':
        student_level = request.GET.get('student_level')
        student_number = request.GET.get('student_number')
        student_name = request.GET.get('student_name')
        student_nickname = request.GET.get('student_nickname')
        student_birthdate = request.GET.get('student_birthdate')
        student_contact = request.GET.get('student_contact')
        student_leader = request.GET.get('student_leader')
        student_contactleader = request.GET.get('student_contactleader')
        student_network = request.GET.get('student_network')
        id = request.GET.get('student_number')
        student_instance = Students.objects.get(student_number=id)
        student_instance.student_level = student_level
        student_instance.student_number = student_number
        student_instance.student_name = student_name
        student_instance.student_nickname = student_nickname
        student_instance.student_birthdate = student_birthdate
        student_instance.student_contact = student_contact
        student_instance.student_leader = student_leader
        student_instance.student_contactleader = student_contactleader
        student_instance.student_network = student_network
        student_instance.save()        
        if Students.objects.filter(student_number = student_number).exists():
            messages = "Student " + student_number +" editted successfully."
        else:
            messages = "Failed to edit student " + student_number
    return JsonResponse({'message': messages})

def lifeclassstudents(request):
    students = Students.objects.filter(student_level="lifeclass")
    return render(request, 'lifeclass_student.html', {'students': students})

def sol1students(request):
    students = Students.objects.filter(student_level="sol1")
    return render(request, 'sol1_student.html', {'students': students})

def sol2students(request):
    students = Students.objects.filter(student_level="sol2")
    return render(request, 'sol2_student.html', {'students': students})

def searchStudent(request):
    if request.method == 'GET':
        student_searchnum = request.GET.get('student_searchnum')
        try:
            student_instance = Students.objects.get(student_number = student_searchnum) 
        except Students.DoesNotExist:
            try:
                student_instance = Students.objects.get(student_name = student_searchnum)
            except Students.DoesNotExist:
                student_instance = None

        if student_instance == None:
            message = "Enter student number or student name only"
        else:
            message = "success"

        return_data = {
            'message' : message,
            'student_level' : student_instance.student_level,
            'student_number' : student_instance.student_number,
            'student_name' : student_instance.student_name,
            'student_nickname' : student_instance.student_nickname,
            'student_birthdate' : student_instance.student_birthdate,
            'student_contact' : student_instance.student_contact,
            'student_leader' : student_instance.student_leader,
            'student_contactleader' : student_instance.student_contactleader,
            'student_network' : student_instance.student_network
        }
        return JsonResponse(return_data)

def home(request):
    try:
        studentnum = Students.objects.latest().student_number
        studentnum = int(studentnum[-3:]) + 1
        studentnum = '%03d' % studentnum
    except Students.DoesNotExist:
        studentnum = '000'
    return render(request, 'code_home.html', {'studentnum':studentnum})