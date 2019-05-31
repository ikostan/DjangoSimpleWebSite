from django.conf.urls import url
from . import views


urlpatterns = [url(r'^$', views.index, name='index')]


#from django.conf.urls import re_path
#from . import views

#urlpatterns = [
#    re_path('', views.index, name='index')]
