"""
URL configuration for Lab_home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Web_home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', views.home),
    path('admin/',views.admin),
    path('research/',views.research_dir),
    path('team/',views.team_t_s),
    path('thesis/',views.thesis),
    path('train/', views.personnel_training),
    path('news/', views.news),
    path('project/', views.project),
    path('patents/', views.patents),
    path('writings/', views.writings),
    path('call_us/', views.call_us)

]
