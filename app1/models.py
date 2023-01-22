from django.db import models
from django.core.exceptions import ValidationError
class Student(models.Model):
    category = (
        
        ('MTech','MTech'),
        ('BTech','BTech'),
        ('Ph.D','Ph.D'),
    )
    First_name = models.CharField(max_length=200,null=True)
    Last_name = models.CharField(max_length=200,null=True)
    Password = models.CharField(max_length=200,null=True)
    Confirm_Password = models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=200,null=True)
    Select_Degree=models.CharField(max_length=200,choices=category,null = True)
    Program_Of_Study = models.CharField(max_length=200,null=True)
    Graduation_year = models.DateField(null = True)
    date_created = models.DateTimeField(auto_now_add=True,)
    
    def __str__(self):
        return self.First_name

    def isobjExists(self):
        if Student.objects.filter(Email=self.Email):
            return True
        else:
            return False
    
        

