from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Project, Department, Employee
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/apps/')
        else:
            return render(request, 'apps/login.html', {'error': 'Please Enter Valid Username And Passwword'})
    return render(request, 'apps/login.html')


def reg_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['first_name']
        )
        return HttpResponseRedirect('/apps/login/')
    return render(request, 'apps/register.html')


def log_view(request):
    logout(request)
    return HttpResponseRedirect('/apps/login/')


@login_required(login_url='/apps/login/')
def index(request):
    return render(request, 'apps/index.html')


@login_required(login_url='/apps/login/')
def about_view(request):
    return render(request, 'apps/about.html')


@login_required(login_url='/apps/login/')
def project_list(request):
    projects_list = Project.objects.all()
    return render(request, 'apps/project_list.html', {'projects_list': projects_list})


@login_required(login_url='/apps/login/')
def create_project(request):
    if request.method == 'POST' and 'FILES':
        Project.objects.create(
            project_name=request.POST['project-name'],
            project_description=request.POST['project-description'],
            start_date=request.POST['start-date'],
            end_date=request.POST['end-date'],
            project_image=request.FILES['image']
        )
        return HttpResponseRedirect('/apps/projects/')
    return render(request, 'apps/create_project.html')


@login_required(login_url='/apps/login/')
def project_details(request, project_id):
    pro = get_object_or_404(Project, pk= project_id)
    return render(request, 'apps/project_details.html', {'pro': pro})


@login_required(login_url='/apps/login/')
def department(request):
    dept = Department.objects.order_by('-id')
    return render(request, 'apps/department.html', {'dept': dept})


@login_required(login_url='/apps/login/')
def emp_lista(request):
    emp_list = Employee.objects.all()
    return render(request, 'apps/emp_list.html', {'emp_list': emp_list})


@login_required(login_url='/apps/login/')
def create_emp(request):
    dept = Department.objects.all()
    if request.method == 'POST':
        dept = Department.objects.get(department_name=request.POST['department'])
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile_no=request.POST['mobile_no'],
            dob=request.POST['dob'],
            qualification=request.POST['qualification'],
            experience=request.POST['experience'],
            salary=request.POST['salary'],
            image=request.FILES['image'],
            department=dept,
        )
        return HttpResponseRedirect('/apps/emp_list')
    return render(request, 'apps/create_emp.html', {"dept": dept})


@login_required(login_url='/apps/login/')
def about_emp(request, emp_id):
    emp = get_object_or_404(Employee, pk=emp_id)
    return render(request, 'apps/about_emp.html', {'emp': emp})


@login_required(login_url='/apps/login/')
def dep_emp_list(request, department_id):
    d = Department.objects.get(pk=department_id)
    dep_emp = Employee.objects.filter(department=d)
    return render(request, 'apps/dep_emp.html', {'dep_emp': dep_emp, "dep":d})


@login_required(login_url='/apps/login/')
def edit_emp_details(request, emp_id):
    emp = Employee.objects.get(id =emp_id)
    if request.method == 'POST':
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.mobile_no = request.POST['mobile_no']
        emp.experience = request.POST['experience']
        emp.salary = request.POST['salary']
        emp.save()
        return HttpResponseRedirect('/apps/emp_list')
    return render(request, 'apps/edit.html', {'emp': emp})


def delete_view(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    emp.delete()
    return HttpResponseRedirect('/apps/emp_list/')

