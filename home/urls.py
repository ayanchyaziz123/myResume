from home.views import home
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('cv/', views.cv, name='cv'),
    path('hireMe', views.hireMe, name='hireMe'),
    path('contactMe', views.contactMe, name='contactMe'),
    path('fullProject/<str:slug>', views.fullProject, name='fullProject'),
]
