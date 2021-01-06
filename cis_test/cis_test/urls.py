"""cis_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="homepage"),
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path('user_login',views.user_login,name='user_login'),
    path('logout', views.user_logout, name='logout'),
    path('product', views.product, name='product'),
    path('get_products', views.get_product, name='get_product'),
    path('update_products/<int:id>', views.update_product, name='update_products'),
      path('delete/<int:id>', views.destroy),  
]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)