from django.contrib import admin
from .models import CustomUser, Group, EmailVerification, CheckGr, GrCode, RoleUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Group)
admin.site.register(GrCode)
admin.site.register(CheckGr)
admin.site.register(EmailVerification)
admin.site.register(RoleUser)
