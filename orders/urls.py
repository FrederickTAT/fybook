from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^create/$',views.create_order),
    url(r'^delet/$',views.del_order),
    url(r'^getorder/$',views.get_order),
    url(r'^makedeal/$',views.make_deal),
    url(r'^canceldeal/$',views.cancel_deal),
]