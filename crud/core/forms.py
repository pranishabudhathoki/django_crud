from django import forms
from .models import Employee


class AddFrom(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ["firstName", "lastName", "phone",
                  "hireDate", "job", "markAttendance", "task"]
