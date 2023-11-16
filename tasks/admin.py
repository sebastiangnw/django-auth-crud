""" Admin site """

from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """ TaskAdmin """
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(Task, TaskAdmin)
