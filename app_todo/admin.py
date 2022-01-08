from django.contrib import admin
from . models import Notification, Task, Complaint
# Register your models here.

admin.site.register(Task)
admin.site.register(Complaint)
admin.site.register(Notification)