from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^landing$', views.Landing.as_view(), name='landing'),
    url(r'^register$', views.Register.as_view(), name='register'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^index$', views.Index.as_view(), name='index'),
]