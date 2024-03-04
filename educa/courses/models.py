from django.db  import models
from django.contrib.auth.models import User



class Subject(models.Model):
    title =  models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    
    class Meta:
        ordering = ['title']
        
    def  __str__(self):
        return self.title
    
    
    


class Course(models.Model):
    owner = models.ForeignKey(User,related_name='courses_created',on_delete=models.CASCADE)
    #The instructor who created  this course
    
    
    subject  = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    #The subject that this course  belongs  to, it is a ForeignKey field that points
    #to the subject model
    title  = models.CharField(max_length=200)
    #The title of the course
    slug = models.SlugField(max_length=200, unique=True) 
    # slug of the course ,it will be used in URLs later  
    overview  = models.TextField()
    #A TextField column to store an overview of the course
    created = models.DateTimeField(auto_now_add=True)  
    #The date and time when the course was created .it will be automatically set by Django
    #when creating new objects because of auto_now_add=True
    
    
    class  Meta:
        ordering = ['-created']
        
        
        def __str__(self):
            return self.title
        
        
        
class Module(models.Model):
    course  = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    
    
    title  = models.CharField(max_length=200)
    description  = models.TextField(blank=True)        
    
    
    def  __str__(self):
        return self.title