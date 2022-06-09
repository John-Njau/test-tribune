"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# re_path -- regex exp
from django.contrib import admin
from django.urls import include
from django.urls import path
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    # path('accounts/',include('django_registration.backends.one_step.urls')),
    # path('accounts/',include('django.contrib.auth.urls')),
    path('tinymce/',include('tinymce.urls')),
    path('logout/',auth_views.LogoutView.as_view(), {'next_page':'/'}),
    path('accounts/', include('registration.backends.simple.urls')),
    # url(r'^logout/$', LogoutView.as_view(template_name='/'), name="logout"),
    # url(r'^login/$', LoginView.as_view(template_name='/login'), name="logout"),

]