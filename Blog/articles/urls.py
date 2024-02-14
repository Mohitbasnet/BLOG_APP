from . import views

from django.urls import path

urlpatterns = [
    
    path('',views.article_list,name = 'artticle-list'),
    path('articles/<slug:slug>/',views.article_detail,name = 'article-detail'),
    path('login/',views.user_login, name = 'login'),
    path('register/', views.user_register, name = 'register')
]
