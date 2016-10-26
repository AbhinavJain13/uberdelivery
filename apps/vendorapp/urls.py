from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^next$', views.next, name="next"),
    url(r'^register$', views.register, name = "register"),
]
