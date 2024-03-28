from django.contrib import admin
from django.urls import path, include  # make sure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Include your app's urls.py here
]
