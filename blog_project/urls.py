
# 文件路径：blog_project/urls.py
from django.contrib import admin
from django.urls import path, include          # 导入 include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),            # 将 blog 应用的路由接入根路径
]