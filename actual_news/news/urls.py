from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page>/', views.index_pagination, name='index_pagination'),
    path('category/<int:pk>/', views.category, name='category'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('me/', views.my_profile, name='my_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('article/<int:pk>', views.article_view, name='article'),
    path('delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),

]

# #6e6e6e