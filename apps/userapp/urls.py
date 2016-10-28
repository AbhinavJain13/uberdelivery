from django.conf.urls import url,include
# from django.contrib import admin
from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^show$',views.show,name="show"),
    url(r'^register$',views.register,name="register"),
    url(r'^code$',views.code,name="code"),
    url(r'^filter_rest$',views.filter_rest,name="filter_rest"),

]
