from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('playlist/<int:id>/<str:name>',views.playlist,name="playlist"),  
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('create_playlist/',views.create_playlist,name="create_playlist"),
    path('create_song/',views.create_song,name="create_song"),
    path('edit/<int:id>',views.edit,name="edit"),

]