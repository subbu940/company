from django.urls import path
from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_view, name='about'),
    path('create_project/', views.create_project, name='create-project'),
    path('projects/', views.project_list, name='projects'),
    path('<int:project_id>/', views.project_details, name='project-details'),
    path('department/', views.department, name='department'),
    path('emp_list/', views.emp_lista, name='emp_list'),
    path('create_emp/', views.create_emp, name='create_emp'),
    path('<int:emp_id>/details/', views.about_emp, name='about_emp'),
    path('<int:department_id>/dep_emp/', views.dep_emp_list, name='dep_emp'),
    path('edit/<int:emp_id>/', views.edit_emp_details, name='edit'),
    path('login/', views.login_view, name='login'),
    path('register/', views.reg_view, name='reg'),
    path('logout/', views.log_view, name='logout'),
    path('delete/<int:emp_id>/', views.delete_view, name='delete')
]