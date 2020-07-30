
from django.contrib import admin
from django.urls import path
import myapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home,name = "home")
    #path('조건(url code)',앱 프로젝트함수 경로 , name = "함수 이름")
    #name 을 설정하는 이유 -> url 과 함수를 구분하고 일치 시키기 위해 url 고장을 방지
    
]
