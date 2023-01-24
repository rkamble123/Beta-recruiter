from django.urls import path
from users import views

urlpatterns = [

    # users
    path('user/',views.UserListCreateApi.as_view(),name='UserListCreateApi'),
    path('user/<int:pk>',views.UserDetailUpdateApi.as_view(),name='UserDetailUpdateApi'),


    # Teams
    path('teams/',views.TeamsListCreateApi.as_view(),name='TeamsListCreateApi'),
    path('teams/<int:pk>',views.TeamsDetailUpdateApi.as_view(),name='TeamsDetailUpdateApi'),


]