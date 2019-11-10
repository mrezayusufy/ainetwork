"""ainetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
app_name = 'main'
urlpatterns = [
    path('admin/', include([
        path('', views.dashboard, name='dashboard'),
        path('login/', views.login, name='login'),
        path('servers/', views.servers, name='server'),
        path('routers/', views.routers, name='router'),
        path('switches/', views.switches, name='switch'),
        path('firewalls/', views.firewall, name='firewall'),
    ])),
    path('blog/', views.blog_index, name='blog_index')
]
