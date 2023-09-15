from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User


# Create your models here.
class Companies(models.Model):
    Company=models.CharField(max_length=250)
    
    Address1=models.CharField(max_length=500)
    
    Address2=models.CharField(max_length=500)
    
    Address3=models.CharField(max_length=500)
    
    Phone=models.CharField(max_length=100)
   
    Email=models.EmailField(max_length=100)
    
    Website=models.CharField(max_length=100)
    
    Logo=models.ImageField()

    def __str__(self):
        return self.Company
    

    class Meta:
        verbose_name_plural = "A. Company"

class State(models.Model):
    State=models.CharField(max_length=250)
    def __str__(self):
        return self.State
    
    class Meta:
        verbose_name_plural = "B. State"
    

class District(models.Model):
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    District=models.CharField(max_length=250)
    def __str__(self):
        return self.District
    
    class Meta:
        verbose_name_plural = "c. District"
    

class Branche(models.Model):
    Branch=models.CharField(max_length=250)
    Branch_code=models.CharField(max_length=250)
    Address=models.CharField(max_length=250,blank=True)
    Street=models.CharField(max_length=250,blank=True)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    district=ChainedForeignKey(District,
                               chained_field="State",
                               chained_model_field="State",
                               show_all=False,
                               auto_choose=False,
                               sort=True,
                               verbose_name= "District")
    Pincode=models.CharField(max_length=12,blank=True)
    Mobile=models.CharField(max_length=25)
    Email=models.EmailField(blank=True)
    

    def __str__(self):
        return self.Branch
    
    class Meta:
        verbose_name_plural = "d. Branch"



class Enquiry_source(models.Model):
    Enquirysourcename=models.CharField(max_length=250)
    def __str__(self):
        return self.Enquirysourcename
    Active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural ="E. Enquiry source"

Followupstatuschoices=(("Yes","Yes"),("No","No"))    

class Follow_up_status(models.Model):
    Followupstatusname=models.CharField(max_length=150)
    def __str__(self):
        return self.Followupstatusname
    Followupstatus=models.CharField(max_length=35,
                                    choices=Followupstatuschoices,default=1)
    Active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "F. Follow up status"

class Qualification(models.Model):
    Qualificationname=models.CharField(max_length=250)
    def __str__(self):
        return self.Qualificationname
    Active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "G. Qualification"

class Syllabus(models.Model):
    syllabus=models.CharField(max_length=1000)
    def __str__(self):
        return self.syllabus
    Active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural ="H.  Syllabus"

class MasterData(models.Model):
    Name=models.CharField(max_length=250)
    value=models.CharField(max_length=250)
    Type=models.CharField(max_length=250)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Name},{self.value},{self.Type}"
    
    class Meta:
        verbose_name_plural ="I.  Master Data"


class Courses(models.Model):
    Course=models.CharField(max_length=250)
    Coursecode=models.CharField(max_length=250)


    def __str__(self):
        return self.Course
    class Meta:
        verbose_name_plural ="J.  Course"
        
class Batch(models.Model):
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Trainer=models.OneToOneField(User,on_delete=models.CASCADE)
    Start_date=models.DateField()
    End_date=models.DateField()
    Closed=models.BooleanField()
    Active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural ="K.  Batch"