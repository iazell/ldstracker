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
    return render(request, 'home.html', {'form': form})

def generate(request):
    if request.method == 'GET':
        student_number = request.GET.get('student_number')
        student_name = request.GET.get('student_name')
        student_nickname = request.GET.get('student_nickname')
        student_birthdate = request.GET.get('student_birthdate')
        student_contact = request.GET.get('student_contact')
        student_leader = request.GET.get('student_leader')
        student_contactleader = request.GET.get('student_contactleader')
        student_network = request.GET.get('student_network')
        qr_code = CodeGenerator(student_number, student_name, student_nickname, student_birthdate, student_contact, student_leader, student_contactleader, student_network)
        buffered = BytesIO()
        qr_code.save(buffered)
        code_64_encode = base64.b64encode(buffered.getvalue())
        code_instance = Codes.objects.create(
            code_bytes = code_64_encode
        )
        return JsonResponse({'code': str(code_64_encode, 'utf-8'), 'id': code_instance.id})

def print(request):    
        if request.method == 'GET':
            data_id = request.GET.get('data')
            data = Codes.objects.get(id = data_id).code_bytes
            fh = open(''.join([str(data_id), '.png']), "wb")
            fh.write(base64.b64decode(data[2:(len(data) - 1)]))
            fh.close()
            isfile = False
            delim = True
            fname = ''.join([str(data_id), '.png'])
        return JsonResponse({'message': 'Success!'})


def addstudent(request):
    if request.method == 'POST':
        student_number = request.POST.get('student_number', None)
        student_name = request.POST.get('student_name', None)
        student_nickname = request.POST.get('student_nickname', None)
        student_birthdate = request.POST.get('student_birthdate', None)
        student_contact = request.POST.get('student_contact', None)
        student_leader = request.POST.get('student_leader', None)
        student_contactleader = request.POST.get('student_contactleader', None)
        student_network = request.POST.get('student_network', None)
        agent_instance = Students.objects.create(
            student_number = student_number,
            student_name = student_name,
            student_nickname = student_nickname,
            student_birthdate = student_birthdate,
            student_contact = student_contact,
            student_leader = student_leader,
            student_contactleader = student_contactleader,
            student_network = student_network
        )
        
        if Students.objects.filter(student_number = student_number).exists():
            string1 = ["Success"]
            messages.success(request, string1)
        else:
            string1 = ['Failed to add student']
            messages.error(request, string1)
    return HttpResponseRedirect('/studentstab/')

def studentstab(request):
    students = Students.objects.all()
    return render(request, 'student.html', {'students': students})

def home(request):
    return render(request, 'code_home.html')
