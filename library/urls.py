from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^search/$',views.search),
    url(r'^append/$',views.append),
    url(r'^remove/$',views.remove),
    url(r'^$',views.library),
]



