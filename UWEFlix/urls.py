from django.urls import path
from UWEFlix import views

# Establish the URLs
urlpatterns = [
    path("", views.student_view, name="home"),
    path("cinema_management/", views.cinema_management_view, name="cinema_management"),
    path("account_management/", views.account_management_view, name="account_management"),
    path("representative/", views.representative_view, name="representative"),
]