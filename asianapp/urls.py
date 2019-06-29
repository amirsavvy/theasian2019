
from asianapp import views
from django.conf.urls import url


urlpatterns = [
    # url(r'^index$', views.home, name='index'),
    #url(r'^', views.home, name='home'),
    url(r'^about-us/', views.aboutus, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^video/detail/(?P<pk>\d+)/$', views.video_details, name='video_detail'),
    url(r'customeremail', views.customer_email, name='customeremail'),


]
