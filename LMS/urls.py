"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from LMS.views import views,user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.Base,name="base"),
    path('404',views.PageNotFound,name="404"),
    path('',views.Home,name="home"),
    path('courses/',views.Single_Course,name="course"),
    path('courses/<slug:slug>',views.Course_Details,name="course_details"),
    path('about_us/',views.About_Us,name="about_us"),
    path('contact_us/',views.Contact_Us,name="contact_us"),
    path('accounts/register/',user_login.Register,name = "register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login',user_login.DoLogin,name="dologin"),
    path('accounts/logout/',user_login.Logout,name="logout"),
    path('accounts/profile/',user_login.Profile,name="profile"),
    path('accounts/profile/update',user_login.Profile_update,name="profile_update"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)