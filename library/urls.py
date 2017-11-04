from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^booksearch/$',views.book_search),
    url(r'^bookadd/$',views.book_add),
    url(r'^bookremove/$',views.book_remove),
    url(r'^commentsearch/$',views.comment_search),
    url(r'^commentadd/$',views.comment_add),
    url(r'^commentremove/$',views.comment_remove),
    url(r'^$',views.library),
]



