from django.urls import path
from . import views


urlpatterns = [
    path("",views.main,name = 'Home'),
    path("about/",views.about, name ="About"),
    path('register/', views.register, name = 'Register' ),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),

]