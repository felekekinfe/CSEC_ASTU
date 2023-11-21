from django.db import models
from django.contrib.auth.models import AbstractUser


class Members(AbstractUser):
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=100)
    Roll=models.CharField(max_length=200)
   

    
    # REQUIRED_FIELDS=['first_name','last_name']
    # objects=MemberManager()

    
    
    def __str__(self):
        
        return self.first_name
    

    class Meta: 
        verbose_name_plural='Members'