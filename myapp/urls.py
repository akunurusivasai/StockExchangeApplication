from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'myapp'
urlpatterns = [
    url(r'^explore/$', views.explore, name='explore'),
    path('plot/<str:name>', views.plot, name='plot'),
    path('fetch/<str:name>/<str:sym>',views.fetch),
    path('dashboard/',views.dashboard),
    path('wallet/',views.wallet),
    path('watchlist/<str:name>',views.watchlist)
]
