from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.advocates.api.routers')),
    path('', views.getRoutes),
]
