from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookieapp/', include('cookieapp.urls')),  # Routes for cookieapp
    path('ex5/', include('ex5.urls')),   
    path('',include('ex3.urls')),            # Routes for ex5
]
