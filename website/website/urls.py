"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


# from django.urls import
# from . import views


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     # url(r'^$', views.index, name="index", ),
#     url('home/', include('home.urls'))
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^blog/', include('blogs.urls')),
    url(r'^contact/', include('contacts.urls')),
    url(r'^', include('home.urls')),
]

print("hello worldXXX")

urlpatterns += staticfiles_urlpatterns()
print("hello world")
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
