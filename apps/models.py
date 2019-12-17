from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=59)
    project_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.project_name


class Department(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    qualification = models.CharField(max_length=50)
    experience = models.CharField(max_length=30)
    salary = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Project = models.ManyToManyField(Project)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
