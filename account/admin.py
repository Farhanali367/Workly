from django.contrib import admin
from account.models import *
# Register your models here.
admin.site.register(user)
admin.site.register(jobseeker)
admin.site.register(company)
admin.site.register(departments)
admin.site.register(Chat)
admin.site.register(Requests)