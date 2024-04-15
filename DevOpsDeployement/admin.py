from django.contrib import admin
from DevOpsDeployement.models import DevOpsStudents
# Register your models here.

class DevOpsAdmin(admin.ModelAdmin):
    pass


admin.site.register(DevOpsStudents, DevOpsAdmin)
