from django.urls import path
from . import views

app_name='First_App'


urlpatterns=[
    path('',views.table, name='table'),
    path('form_contact/', views.form_contact, name='form_contact'),
]