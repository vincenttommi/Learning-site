from django.db import models
from django.core.exceptions import ObjectDoesNotExist




class  OrderField(models.PositiveBigIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields  = for_fields
        super().__init__(*args, **kwargs)
        
        
        
        
    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is  None:
            #no current value
            #checking if the a value already exists  for the field in model instance
            
            try:
                qs = self.model.objects.all()
                #a query set to retrieve all objects for the field model
                if self.for_fields:
                    #filter by objects with the same field values
                    #for the fields in "for_fields"
                    query  = {field: getattr(model_instance, field)   for field in self.for_fields}
                    qs  = qs.filter(**query)
                
                    #getting the order of the last item
                    
                    last_item = last_item.order + 1
                    value = last_item.order + 1
                    
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return  value
        else:
            return  super().pre_save(model_instance,add)