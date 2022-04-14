from urllib import response
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Employee
from .forms import AddFrom
# Create your views here.


class Home(View):
    def get(self, request):
        emp_data = Employee.objects.all()
        return render(request, 'core/home.html', {'empdata': emp_data})


class Add_Intern(View):
    def get(self, request, *args, **kwargs):
        fm = AddFrom(request.POST)
        if request.method == "POST":
            if fm.is_valid():
                fm.save()
                return redirect('home')

        return render(request.POST, 'core/add.html', {'form': fm}),
