from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^welcome', views.welcome, name='welcome'),
    url('^pledge', views.pledge_user_to_event, name='pledge'),
    url('^cancel_pledge', views.cancel_pledge, name='cancel_pledge'),

    url(r'^login?/',
        auth_views.login,
        {'template_name': 'login.html'},
        name='auth_login'),
    url(r'^logout?/',
        auth_views.logout,
        {'template_name': 'logout.html'},
        name='auth_logout'),
]

