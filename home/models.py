from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N','not to disclose')
    )
    
class Book(models.Model):

    
    name = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class School(models.Model):

    
    name = models.CharField(max_length=300)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    is_active =models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
        
class Student(models.Model):
    

    first_name =models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=254,blank=False)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1,default='N')
    school = models.ForeignKey(School,blank=False,on_delete=models.PROTECT)
    book = models.ForeignKey(Book,blank=False,on_delete=models.PROTECT)
    pages_read_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name