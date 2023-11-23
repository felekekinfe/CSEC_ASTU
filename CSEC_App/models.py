from django.db import models
from django.contrib.auth.models import AbstractUser



class Members(AbstractUser):
    
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=100)
    Roll=models.CharField(max_length=200)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='profile_image')
    
    
    
    def __str__(self):
        
        return self.first_name
    

    class Meta: 
        verbose_name_plural='Members'

class Events(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    date=models.DateTimeField()
    time=models.TimeField()
    venue=models.CharField(max_length=200)
    organizer=models.CharField(max_length=100,default="CSEC_Dev")
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Events'
        
    def __str__(self):
        return self.title
