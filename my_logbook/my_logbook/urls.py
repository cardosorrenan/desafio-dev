from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('app.urls')),
    path('api/v1/', include('api.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]
