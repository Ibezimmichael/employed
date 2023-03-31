from django.urls import path
from . import views


urlpatterns = [
    path("homepage/", views.homepage, name="employees_home"),
    path('', views.EmployeeList.as_view(), name='all_employees'), 
    path('<name>', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('delete/<name>', views.EmployeeDetailDelete.as_view(), name='employee_delete'),
    path('by-department/<department>/', views.EmployeesByDepartment.as_view(), name='employees_by_department')

    
]
