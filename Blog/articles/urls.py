from . import views

from django.urls import path
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView


urlpatterns = [
    
    path('',views.article_list,name = 'article-list'),
    path('articles/<slug:slug>/',views.article_detail,name = 'article-detail'),
    # path('login/',views.user_login, name = 'login'),
    path('login/',LoginView.as_view(), name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/',PasswordChangeDoneView.as_view(),name = 'password_change_done'),
    path('register/', views.user_register, name = 'register')
]
