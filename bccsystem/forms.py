from django import forms

class StudentForm(forms.Form):
    student_number = forms.CharField(label='Student Number', max_length=13)
    student_name = forms.CharField(label='Name', max_length=13)
    student_nickname = forms.CharField(label='Nickname', max_length=60)
    student_birthdate = forms.CharField(label='Birthdate', max_length=60)
    student_contact = forms.CharField(label='Contact Number', max_length=13)
    student_leader = forms.CharField(label='Cell Leader', max_length=13)
    student_contactleader = forms.CharField(label='Contact Number of CL', max_length=60)
    student_network = forms.CharField(label='Network', max_length=60)