from django.urls import path
from .views import (
    about,
    certifications,
    contact,
    education,
    experience,
    home,
    projects,
    skills,
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),
    path('education/', education, name='education'),
    path('certifications/', certifications, name='certifications'),
    path('experience/', experience, name='experience'),
    path('contact/', contact, name='contact'),
]
