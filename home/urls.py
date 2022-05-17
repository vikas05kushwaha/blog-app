"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("about",views.about,name='about'),
    # path("services/",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    # path("sold_book",views.sold_book,name='sold_book'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),
    path('blogs', views.blogs,name="blogs"),
    # path('jeanspost', views.jeanspost,name="jeanspost"),
    path('blogpost/<int:idd>', views.blogpost,name="blogpost"),
    path('tag', views.tag,name="tag"),
    path('blogform',views.blogform,name="blogform"),
    # path('myhome',views.myhome,name="myhome"),
    # path('jeansform',views.jeansform,name='jeansform'),
    path('blogpostdelete/<int:idd>', views.blogpostdelete,name="blogpostdelete"),
    path('blogpostupdate/<int:idd>', views.blogpostupdate,name="blogpostupdate"),
    path("track",views.track,name="track")
    # path("staff",views.staff,name="name")
    # path("ana",views.ana,name="ana")
    
 
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)