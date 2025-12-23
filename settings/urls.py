from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.tickets.urls')),
    path('users/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
]
