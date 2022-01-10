from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logged-out', views.logging_out_view, name='logout'),
    path('signup', views.sign_up_view, name='signup'),
    path('complaint/<int:id>', views.view_complaint_byid, name='view_complaint'),
    path('edit/<int:id>',views.edit_complaint_byid,name='edit_complaint'),
    path('edit/<int:id>',views.edit_complaint_byid,name='edit_dialog'),
    path('delete/<int:cmp_id>', views.delete_complaint_byid, name='delete_complaint')
]

