"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

## 프로젝트 수준의 경로 패턴 정의
from django.contrib import admin
from django.urls import path, include # include(): 다른 urls.py파일을 참조할 수 있도록 함

urlpatterns = [
    path('survey/', include('survey.urls')), # 어떤 주소에 접속할 때 survey/까지 잘라내고 나머지 부분만 survey.urls로 보내줌
    path('admin/', admin.site.urls),
]






















