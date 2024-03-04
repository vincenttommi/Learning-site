from django.contrib import admin
from django.urls import path
from django.conf  import settings
from django.conf.urls.static  import static



urlpatterns = [
    
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
#a helper function to serve  media files with Django development server during development
#suitable for development but not production use 
