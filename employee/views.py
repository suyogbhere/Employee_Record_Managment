from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from employee.models import Employee_Detail,Employee_Experience,Employee_Education
from django.contrib.auth import login, logout, authenticate 

# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ''
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name = fn, last_name= ln, username=em, password=pwd)
            Employee_Detail.objects.create(user=user,empcode=ec)
            Employee_Experience.objects.create(user=user)
            Employee_Education.objects.create(user=user)
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'registration.html',locals())



def emp_login(request):
    error= ''
    if request.method == 'POST':
        U = request.POST['email']
        P = request.POST['pwd']
        user = authenticate(username=U, password=P)
        # print(user)
        if user:
            login(request, user)
            error = 'no'
            # print(error)
        else:
            error= 'yes'
            # print(error)
    return render(request, 'emp_login.html', locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    else:
        return render(request, 'emp_home.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ''
    user = request.user
    employee = Employee_Detail.objects.get(user= user)
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        ec = request.POST['empcode']
        ed = request.POST['designation']
        edep = request.POST['department']
        con = request.POST['contact']
        jd = request.POST['jdate']
        gen = request.POST['gender']
        em = request.POST['email']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.designation = ed
        employee.empdept = edep
        employee.contact = con
        employee.gender = gen

        if jd:
            employee.joining_date = jd
        try:
            employee.save()
            employee.user.save()
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'profile.html',locals())

def Logout(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    logout(request)
    return redirect('index')


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience = Employee_Experience.objects.get(user= user)
    return render(request, 'my_experience.html',locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ''
    user = request.user
    experience = Employee_Experience.objects.get(user= user)
    if request.method == 'POST':
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration
        experience.company2name = company2name
        experience.company2salary = company2salary
        experience.company2desig = company2desig
        experience.company2duration = company2duration
        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        
        try:
            experience.save()
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'edit_my_experience.html',locals())


def edit_experience_admin(request,id):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ''
    user = User.objects.get(pk=id)
    experience = Employee_Experience.objects.get(user= user)
    if request.method == 'POST':
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration
        experience.company2name = company2name
        experience.company2salary = company2salary
        experience.company2desig = company2desig
        experience.company2duration = company2duration
        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        
        try:
            experience.save()
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'edit_experience.html',locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    education = Employee_Education.objects.get(user= user)
    return render(request, 'my_education.html',locals())


def edit_my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ''
    user = request.user
    education = Employee_Education.objects.get(user= user)
    if request.method == 'POST':
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclgra = request.POST['schoolclgra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursegrahsc = request.POST['coursegrahsc']
        schoolclhsc = request.POST['schoolclhsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg
        education.coursegra = coursegra
        education.schoolclgra = schoolclgra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra
        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc
        education.coursegrahsc = coursegrahsc
        education.schoolclhsc = schoolclhsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc
        
        try:
            education.save()
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'edit_my_education.html',locals())


def edit_education_admin(request, id):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ''
    # user = request.user
    user = User.objects.get(pk = id)
    education = Employee_Education.objects.get(user=user)
    if request.method == 'POST':
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclgra = request.POST['schoolclgra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursegrahsc = request.POST['coursegrahsc']
        schoolclhsc = request.POST['schoolclhsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg
        education.coursegra = coursegra
        education.schoolclgra = schoolclgra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra
        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc
        education.coursegrahsc = coursegrahsc
        education.schoolclhsc = schoolclhsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc
        
        try:
            education.save()
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'edit_education_admin.html',locals())



def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ''
    user = request.user
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'
    return render(request, 'change_password.html',locals())


def admin_login(request):
    error= ''
    if request.method == 'POST':
        U = request.POST['username']
        P = request.POST['pwd']
        user = authenticate(username=U, password=P)
        # print(user)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
                # print(error)
            else:
                error= 'yes'
                # print(error)
        except:
            error = 'yes'
    return render(request, 'admin_login.html',locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    else:
        return render(request, 'admin_home.html')
    

def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ''
    user = request.user
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'
    return render(request, 'change_password_admin.html',locals())


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    employee = Employee_Detail.objects.all()
    return render(request, 'all_employee.html',locals())


def edit_profile(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ''
    user = request.user
    employee = Employee_Detail.objects.get(pk= id)
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        ec = request.POST['empcode']
        ed = request.POST['designation']
        edep = request.POST['department']
        con = request.POST['contact']
        jd = request.POST['jdate']
        gen = request.POST['gender']
        em = request.POST['email']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.designation = ed
        employee.empdept = edep
        employee.contact = con
        employee.gender = gen

        if jd:
            employee.joining_date = jd
        try:
            employee.save()
            employee.user.save()
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'edit_profile.html',locals())


def delete_employee(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login') 
    user = User.objects.get(pk=id)
    employee = Employee_Detail.objects.get(user=user)
    employee.delete()
    return redirect('allemp')
