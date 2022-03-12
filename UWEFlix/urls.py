from django.urls import path
from UWEFlix import views

# Establish the URLs
urlpatterns = [
    # path("", views.student_view, name="home"),
    path("", views.student_view, name="home"), #home screen will be placeholder
    path("cinema_management/", views.cinema_management_view, name="cinema_management"),
    path("account_management/", views.account_management_view, name="account_management"),
    path("representative/", views.representative_view, name="represent"),
    path("about/", views.about, name="about"), 
    path("login/", views.login, name="login"), 
    # path("movies/", views.movies, name="movies"), 


]