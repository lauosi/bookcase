from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'bookcase'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^book/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^book/(?P<pk>[0-9]+)/add_review/$', views.AddReview.as_view(), name="add_review"),
    url(r'^book/add/$', views.AddBook.as_view(), name='add_book'),
    url(r'^author/add/$', views.AddAuthor.as_view(), name='add_author'),
    url(r'^author/(?P<pk>[0-9]+)$', views.DetailAuthor.as_view(), name='detail_author'),
]
