from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('/wallfeed',views.wallfeed),
    path('/community',views.community),
    # path('/client_profile/<int:i>',views.client_profile),
    path('/freelancer_profile/<int:i>',views.freelancer_profile),
    # path('/create_post',views.create_post),
    # path('/create_comment',views.create_comment),
    # path('/create_messages',views.create_messages),
    
  
]
