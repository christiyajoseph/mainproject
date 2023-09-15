from django.db import models
from settings.models import Enquiry_source,State,District,Courses,MasterData
from smart_selects.db_fields import ChainedForeignKey

Genderchoices=(("Male","Male"),("Female","Female"))

# Create your models here.
class Student(models.Model):

    
    Enquiry_source=models.ForeignKey(Enquiry_source,on_delete=models.CASCADE)
    student=models.CharField(max_length=250)
    def __str__(self):
        return self.student
    Gender=models.CharField(max_length=10,choices=Genderchoices)
    Dob=models.DateField(max_length=8)
    Email=models.EmailField()
    Phone=models.CharField(max_length=15)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    District=ChainedForeignKey(District,
                               chained_field="State",
                               chained_model_field="State",
                               show_all=False,
                               auto_choose=False,
                               sort=True,
                               verbose_name= "District")
    Course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    
    Photo=models.ImageField()

class FeeDetails(models.Model):
    Studentname=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    feetype=models.ForeignKey(MasterData,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Studentname} - {self.feetype}"
    

class FeeReceipt(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    amount=models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name},{self.amount}"