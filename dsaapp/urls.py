from django.urls import path
from . import views

urlpatterns =[
    path('',views.signup,name='register'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('problems', views.problems, name='problems'),
    path('search', views.search, name='search'),
    path('progress', views.progress, name='progress')
]