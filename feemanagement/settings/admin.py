from typing import Any, List
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from.models import Companies,State,District,Branche,Enquiry_source,Follow_up_status,Qualification,Batch,Syllabus,Courses,MasterData

# Register your models here.
admin.site.register(Companies)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Branche)
admin.site.register(Enquiry_source)
admin.site.register(Follow_up_status)
admin.site.register(Qualification)
admin.site.register(Syllabus)
admin.site.register(MasterData)
admin.site.register(Courses)
admin.site.register(Batch)