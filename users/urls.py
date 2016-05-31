from django.conf.urls import url
from users import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^landing$', views.Landing.as_view(), name='landing'),
    url(r'^register$', views.Register.as_view(), name='register'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
    url(r'^index$', views.Index.as_view(), name='index'),
    url(r'^profile$', views.Profile.as_view(), name='profile'),
    url(r'^upload$', views.ProfileImageView.as_view(), name='profileimage'),
    url(r'^userprefandmatch$', views.UserPrefAndMatch.as_view(), name='userprefandmatch'),
]
# add static file location to use media as static file in production
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)