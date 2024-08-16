from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import app_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('wishes.urls'))
]

