
from django.contrib import admin
from django.urls import path
import myDateapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myDateapp.views.date,name = 'date')
]
