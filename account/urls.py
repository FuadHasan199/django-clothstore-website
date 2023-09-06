from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.usersignup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('logout/',views.userLogout,name='logout'),
    
]
