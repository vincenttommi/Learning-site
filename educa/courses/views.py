from django.shortcuts import render
from .models import Course
from django.views.generic.list import ListView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.urls import  reverse_lazy

# Create your views here.

#class based views
class ManageCourseListView(ListView):
    model = Course
    template_name  = 'courses/manage/course/list.html'
    
    
    def get_querset(self):
        qs = super().get_queryset()
        return  qs.filter(owner=self.request.user)
    #overriding the get_queryset method of the view to retreive only courses  created 
    #by current user
        
    


class OwnerMixin:
    def get_queryset(self):
        qs  = super.get_gueryset()
        return qs.filter(owner=self.request.user)
    
    
    


class ownerEditMixin:
    def  form_valid(self, form):
        form.instance.owner  = self.request.user
        return super().form_valid(form)
    
class  ownerCourseMixin(OwnerMixin):
    model =  Course
    # The model used  for QuerySets, it is used all views
    fields  = ['subject', 'title', 'slug', 'overview']
    #fields  of the model to build  model form of  CreateView and UpdateView views
    success_url  = reverse_lazy('manage_course_list')
    # used by CreateView,UpdateView, and DeleteView to redirect user after
    #the form is successfully submitted or object is deleted
    


class ownerCourseEditMixin(ownerCourseMixin, ListView):
    template_name  = 'courses/manage/course/list.html'
    #will use  the CreateView and UpdateView views
    

class CourseCreateView(ownerCourseEditMixin, CreateView):
    pass
    



class CourseUpdateView(ownerCourseEditMixin, UpdateView):
    pass




class CourseDeleteView(ownerCourseMixin, DeleteView):
    template_name  = 'courses/manage/course/delete.html'
    

        
            
    