from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registration/', views.registration, name= "registration"),
    path('emp_login/', views.emp_login, name= "emp_login"),
    path('emp_home/', views.emp_home, name= "emp_home"),
    path('profile/', views.profile, name= "profile"),
    path('logout/', views.Logout, name= "logout"),
    path('admin_login/', views.admin_login, name= "admin_login"),
    path('my_experience/', views.my_experience, name= "my_experience"),
    path('edit_experience/', views.edit_experience, name= "edit_experience"),
    path('edit_experience_admin/<int:id>/', views.edit_experience_admin, name= "edit_experience_admin"),
    path('my_education/', views.my_education, name= "my_education"),
    path('edit_my_education/', views.edit_my_education, name= "edit_my_education"),
    path('edit_education_admin/<int:id>/', views.edit_education_admin, name= "edit_education_admin"),
    path('changepwd/', views.change_password, name='changepwd'),
    path('admin_home/', views.admin_home, name= "admin_home"),
    path('changepwdadm/', views.change_password_admin, name='changepwdadm'),
    path('allemp/', views.all_employee, name='allemp'),
    path('edit_profile/<int:id>/', views.edit_profile, name= "edit_profile"),
    path('delete_employee/<int:id>/', views.delete_employee, name= "delete_employee"),
]
 