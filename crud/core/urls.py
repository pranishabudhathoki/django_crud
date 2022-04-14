from django.urls import path
from .views import Add_Intern, Home

urlpatterns = [

    path('', Home.as_view(), name='core'),
    path('add/', Add_Intern.as_view(), name='add')
]
