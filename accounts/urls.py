from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='accounts'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^kyc/$', views.kyc),
]
