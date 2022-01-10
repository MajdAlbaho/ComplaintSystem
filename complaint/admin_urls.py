from django.urls import path
from . import views

urlpatterns = [
    path('complaints', views.admin_view_complaints,
         name='admin_complaints_view'),
]