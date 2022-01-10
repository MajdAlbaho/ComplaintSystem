from django.contrib import admin

# Register your models here.
from .models import Complaint, Remark, Profile


admin.site.register(Complaint)
admin.site.register(Remark)
admin.site.register(Profile)
