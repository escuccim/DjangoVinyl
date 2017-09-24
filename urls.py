from django.conf.urls import url
from . import views

app_name = "records"

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', views.Show, name='show'),
]
