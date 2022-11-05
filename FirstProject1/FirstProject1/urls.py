"""FirstProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from MyApps1 import views as v1
from MyApps1 import views as f11
from MyApps1 import views as f22
from MyApps1 import views as v11;
from MyApps1 import views as v22;


urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/',views.display),

    #multiple views
    path('mrng/', v1.f1),
    path('aftr/',v1.f2),
    path('even/',v1.f3),

    path('hello/', f11),
    path('datetime/', f22),

    path('hello1/', v11.f11),
    path('datetime1/', v22.f22),
]
