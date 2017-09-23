from django.conf.urls import url
from . import views

app_name = "records"

urlpatterns = [
    url(r'^$', views.Index, name='index'),
]
