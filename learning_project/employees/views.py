from django.http import HttpResponse
from django.http import JsonResponse
from employees.models import Employee


def index(request):
    emps = Employee.objects.all()
    emp_list = list()
    for emp in emps:
        emp_list.append(emp.to_json())
    return JsonResponse({"items": emp_list})
