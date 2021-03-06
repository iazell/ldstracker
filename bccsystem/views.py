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
from tablib import Dataset

from .forms import StudentForm
from blog.models import Students
from blog.models import AttendanceLifeclass
from blog.models import AttendanceSOL1
from blog.models import AttendanceSOL2
from .codegenerator import CodeGenerator
from blog.models import Network

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .resources import StudentResource


from blog.serializers import StudentsSerializer
from blog.serializers import AttendanceStudentLifeclassSerializer
from blog.serializers import AttendanceStudentSOL1Serializer
from blog.serializers import AttendanceStudentSOL2Serializer

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

        directory = os.path.dirname(os.path.realpath(__file__ ))
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

        filename = os.path.join(directory, student_number)
        fh = open(''.join([filename, '.png']), "wb")
        fh.write(buffered.getvalue())
        fh.close()
        isfile = False
        delim = True
        fname = ''.join([filename, '.png'])

        return JsonResponse({'code': str(code_64_encode, 'utf-8'), 'id': code_instance.id, 'filename': fname})

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
    attendance = AttendanceLifeclass.objects.all()
    return render(request, 'lifeclass_student.html', {'students': students, 'attendance':attendance})

def sol1students(request):
    students = Students.objects.filter(student_level="sol1")
    attendance = AttendanceSOL1.objects.all()
    return render(request, 'sol1_student.html', {'students': students, 'attendance':attendance})

def sol2students(request):
    students = Students.objects.filter(student_level="sol2")
    attendance = AttendanceSOL2.objects.all()
    return render(request, 'sol2_student.html', {'students': students, 'attendance':attendance})

def searchStudent(request):
    if request.method == 'GET':
        student_searchnum = request.GET.get('student_searchnum')
        try:
            student_instance = Students.objects.get(student_number = student_searchnum) 
        except Students.DoesNotExist:
            try:
                student_instance = Students.objects.filter(student_name = student_searchnum).order_by('id').first()
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
        studentnum = Students.objects.filter(student_level="lifeclass").latest().student_number
        studentnum = int(studentnum[-3:]) + 1
        studentnum = '%03d' % studentnum
        networks = Network.objects.all()
    except Students.DoesNotExist:
        studentnum = '000'
        networks = Network.objects.all()
    return render(request, 'code_home.html', {'studentnum':studentnum, 'networks':networks})

class StudentList(ListAPIView):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        queryset = Students.objects.all()
        return queryset

class AttendanceStudentLifeclass(ListCreateAPIView):
    queryset = AttendanceLifeclass.objects.all()
    serializer_class = AttendanceStudentLifeclassSerializer

class AttendanceStudentSOL1(ListCreateAPIView):
    queryset = AttendanceSOL1.objects.all()
    serializer_class = AttendanceStudentSOL1Serializer

class AttendanceStudentSOL2(ListCreateAPIView):
    queryset = AttendanceSOL2.objects.all()
    serializer_class = AttendanceStudentSOL2Serializer

def export(request):
    student_resource = StudentResource()
    dataset = student_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="students.xls"'
    return response

def simple_upload(request):
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read())
        result = student_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            student_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')