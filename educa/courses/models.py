from django.db  import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models  import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



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
    
    
    
    
class  Content(models.Model):
    
    module  = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    #a foriegnkey field to the contentType Model
    content_type  = models.ForeignKey(ContentType, on_delete=models.CASCADE,limit_choices_to={'model__in':(
        'text','video','image','file')})
    object_id  = models.PositiveBigIntegerField()
    #positiveIntegerField to store primary key of  the related object
    item  = GenericForeignKey('content_type', 'object_id')
    #A GenericForeignKey field to related object combining two previous fields
        
        
       
       
       
       
       
#Content model , a module that  contains  multiple contents and entails a foriegnkey field that
#points to  module model 
        
        
        
  
class BaseContent(models.Model):
    title =  models.CharField(max_length=100)
    created  = models.DateTimeField(auto_now_add=True)
    class meta:
        abstract  = True
        



class ItemBase(models.Model):
    owner  = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    
    title  = models.CharField(max_length=250)
    created  = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    
    
    
    class Meta:
        abstract  = True
        
        
        def __str__(self):
            return  self.title
        
        
        
class  Text(ItemBase):
    content  = models.TextField()
    #Stores text content
class  File(ItemBase):
    file  =  models.FileField(upload_to='files')
    # stores files,such as  PDFs
class  Image(ItemBase):
    file  = models.FileField(upload_to='images')
    #Storing image  files
class  Video(ItemBase):
    url  = models.URLField()
    #Storing videos,
    
    
    
    
    
#defining an abstract model named ItemBase and set abstract=True in it's Meta class

 