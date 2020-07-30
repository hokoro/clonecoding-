
from django.contrib import admin
from django.urls import path
import mydate.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mydate.views.date,name = 'date')
]
