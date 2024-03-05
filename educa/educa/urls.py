from django.contrib import admin
from django.urls import path
from django.conf  import settings
from django.conf.urls.static  import static
from django.contrib.auth import views as auth_views




urlpatterns = [
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #django authetication framework for users to authenticate
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    
    path('admin/', admin.site.urls),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
#a helper function to serve  media files with Django development server during development
#suitable for development but not production use 
