
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    
    # handle the incoming request for /admin route
    path('admin/', admin.site.urls),

    # handle the incoming request for / route [stage_1 app]
    path('', include('stage_1.urls')),
]
