
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Aseg�rate de que este sea 'myapp.urls' y no solo 'myapp'
]
