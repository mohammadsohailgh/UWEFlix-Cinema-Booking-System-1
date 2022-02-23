from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import ListView

# Student view presenting the UI to book tickets
def student_view(request):
    return render(request, "UWEFlix/student.html")

# View to provide cinema manager a UI to manage films
def cinema_management_view(request):
    return render(request, "UWEFlix/cinema_manager.html")

# View to provide account manager a UI to manage accounts
def account_management_view(request):
    return render(request, "UWEFlix/account_manager.html")

# View to provide representative a UI to manage films
def representative_view(request):
    return render(request, "UWEFlix/representative.html")