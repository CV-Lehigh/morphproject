"""project URL Configuration

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
from django.urls import path 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import EmployeeImage
from .views import EmpImageDisplay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Showemp, name='index'),
    path('instruction', views.instruction, name='instruction'),
    path('consent', views.consent, name='consent'),
    path('process', views.process_page, name='process'),
    path('post_process', views.post_process, name='post_process'),
    path('upload',EmployeeImage.as_view(), name = 'upload'),
    path('emp-image/<int:pk>/',EmpImageDisplay.as_view(), name = 'display'),
    path('nextimage/<int:pk>/',views.NextImage,name='nextimage'),
    path('uploadMass',views.uploadMass, name='uploadMass'),
    path('allImages',views.allImages,name='allImages'),
    path('do_something',views.do_something, name='do_something')
]
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
