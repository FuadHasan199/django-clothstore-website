from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.usersignup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('logout/',views.userLogout,name='logout'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
]
