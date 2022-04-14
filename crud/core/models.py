
from django.db import models

# Create your models here.


attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)


class Employee(models.Model):
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    hireDate = models.DateField()
    job = models.CharField(max_length=100, null=False)
    markAttendance = models.CharField(
        max_length=8, choices=attendance_choices, blank=True)
    task = models.TextField()

    class Meta:
        db_table = "core_employee"

    def __str__(self):
        return self.firstName
