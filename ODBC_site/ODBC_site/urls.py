"""ODBC_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from odbc import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # main site
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('latest/', views.latest, name='latest'),
    path('watch/', views.watch, name='watch'),
    path('contact/', views.contact, name='contact'),

    # ministries
    path('baptism-ministry/', views.baptism, name='baptism'),
    path('childrens-ministry/', views.children, name='children'),
    path('mens-ministry/', views.mens, name='mens'),
    path('mentorship-ministry/', views.mentorship, name='mentorship'),
    path('womens-ministry/', views.women, name='womens'),
    path('girls-ministry/', views.girls, name='girls'),
    path('camp-ministry/', views.camp, name='camp'),
    
    # backend
    path('odbc-admin/', views.odbc_admin, name='odbc-admin'),
    path('odbc-admin-create/', views.odbc_admin_create, name='odbc-admin-create'),
    path('odbc-admin-update/<int:id>/', views.odbc_admin_update, name='odbc-admin-update'),
    path('odbc-admin-delete/<int:id>/', views.odbc_admin_delete, name='odbc-admin-delete'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
