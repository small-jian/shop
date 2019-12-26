from django.conf.urls import url

from App import views

app_name = 'app'
urlpatterns = [
    url('^index/',views.index),
    url('^login/',views.login,name='login')
]