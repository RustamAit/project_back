from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Expert)
admin.site.register(Assignee)
admin.site.register(BecomeAssigneeRequest)
