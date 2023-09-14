from django.urls import path
from . import views

app_name = 'Web'

urlpatterns = [
    path("", views.home, name="index"),
    path("home/", views.home, name="home"),
    path("research/", views.research_dir, name="admin"),
    path("team/", views.team_t_s, name="team.html"),
    path("thesis/", views.thesis, name="thesis"),
    path('train/', views.personnel_training, name="personnel_training"),
    path('news/', views.news, name="news"),
    path('news/detail/<int:news_id>', views.news_detail, name="news_detail"),
    path('project/', views.project, name="project"),
    path('patents/', views.patents, name="patents"),
    path('writings/', views.writings, name="writings"),
    path('contactus/', views.contactus, name="contactus"),
    path('test/', views.test)
]
