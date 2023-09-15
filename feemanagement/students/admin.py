from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.urls import NoReverseMatch
from django import forms
from .models import *
from feemanagement.widgets import PastCustomDatePickerWidget


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('Enquiry_source',),
        }),
        ('Personal Info', {
            'fields': (('student','Gender'),'Dob',('Email','Phone'),('State', 'District',)),
               
        }),
        ('Course Info', {
            'fields': ('Course',),
        }),
        ('Photo', {
            'fields': ('Photo',),
        }),
        
)


    formfield_overrides={
        models.DateField: {'widget': PastCustomDatePickerWidget},
    }

    list_display=('student','Course','fees_link')

    def fees_link(self,obj):
        try:
            url= f"/admin/students/feedetails/?Studentname={obj.id}"
            link = f'<a href="{url}">Go</a>'
            return format_html(link)
        except NoReverseMatch:
            return None

    fees_link.short_description='Fees'
    fees_link.allow_tags= True


class FeeDetailsAdmin(admin.ModelAdmin):
    list_display=('Studentname','feetype','payment')

    def payment(self,obj):
        try:
            url= f"/admin/students/feereceipt/add/?name={obj.id}"
            link = f'<a href="{url}">Pay</a>'
            return format_html(link)
        except NoReverseMatch:
            return None

    payment.short_description='receipt'
    payment.allow_tags= True

    



class FeeReceiptAdmin(admin.ModelAdmin):
    list_display=('name','amount')

admin.site.register(Student,StudentAdmin)
admin.site.register(FeeDetails,FeeDetailsAdmin)
admin.site.register(FeeReceipt,FeeReceiptAdmin)
