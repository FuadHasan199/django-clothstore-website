
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('category/<slug:category_slug>',views.home,name='category_products'),
    path('<int:product_id>',views.details,name='details'),
    path('review/<int:product_id>/create/',views.create_review,name='review'),
    path('filter/', views.filter, name='filter'),

]