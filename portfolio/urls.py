from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('regression/', views.regression, name='regression'),
    path('classification/', views.classification, name='classification'),
    path('clustering/', views.clustering, name='clustering'),
    path('dimensionality_reduction/', views.dimensionality_reduction, name='dimensionality_reduction'),
    path('about_me/', views.about, name='about_me'),
]
