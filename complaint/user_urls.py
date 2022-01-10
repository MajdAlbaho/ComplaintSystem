from django.urls import path
from . import views

urlpatterns = [
    path('complaints', views.user_view_complaints,
         name='user_complaints_view'),

    path('register_complaint', views.register_complaint_page,
          name='register_complaint'),
     path('change-password', views.change_password_view, name='change-password'),

]
