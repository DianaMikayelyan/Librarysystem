from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library'),
    path('user/', views.user_profile, name='user_profile'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'), 
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('download/<int:book_id>/', views.download_book, name='download_book'),
    path('read/<int:book_id>/', views.read_book, name='read_book'),
    path('logout/', views.logout_view, name='logout'),
]