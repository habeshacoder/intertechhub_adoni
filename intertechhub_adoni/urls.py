
from django.contrib import admin

from drf_spectacular.views \
    import SpectacularAPIView, SpectacularSwaggerView

from django.urls import path, include

urlpatterns = [

    # handle the incoming request for /admin route
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    # path('', include('stage_1.urls')),
    path('', include('stage_2.urls')),
]
