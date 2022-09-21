from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('follow', views.follow, name='follow'),
    path('like_post', views.likes, name='like_post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('delete/<int:pk>', views.delete, name='delete'),

]
