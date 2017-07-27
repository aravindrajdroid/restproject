from django.conf.urls import *
from django.contrib import admin

from restapp import views

admin.autodiscover()

urlpatterns = [
url(r'^admin/', include(admin.site.urls)),
    url(r'^alllang/', views.UserList.as_view()),
    url(r'^addlang/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),]