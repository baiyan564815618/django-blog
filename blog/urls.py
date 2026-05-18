# 文件路径：blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import FavoriteListView

urlpatterns = [
    # CBV：类后面加 .as_view() 将其转为视图函数
    path('', views.PostListView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('favorites/', FavoriteListView.as_view(), name='favorites'),
    # 其他视图不变
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
]