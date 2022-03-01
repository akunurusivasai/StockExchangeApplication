from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^index/', include('myapp.urls')),
    url(r'^home/', views.home,name='home'),
    url(r'^support/', views.support),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
