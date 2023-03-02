
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.regsier_view),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view),
    path('', views.dashboard_view,name='dashboard'),


]
