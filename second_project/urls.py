"""second_project URL Configuration

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
from django.contrib import admin
from django.urls import path
from second_app import views as sa_view
from timeApp import views as ta_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gm/',sa_view.gm_view,name = "GoodMorning"),
    path('ga/',sa_view.ga_view,name = "GoodAfternoon"),
    path('ge/',sa_view.ge_view,name = "GoodEvening"),
    path('time/',ta_view.tellMeTime,name = "Time"),
]
