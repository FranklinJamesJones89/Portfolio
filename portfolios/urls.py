'''Defines URL patterns for portfolios'''

from django.urls import path

from . import views

app_name = 'portfolios'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contactj')
]
