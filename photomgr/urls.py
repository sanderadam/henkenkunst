from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_schilderij, name='add_schilderij'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^overzicht/$', views.overview, name='overview'),
    url(r'^view/(?P<pk>\d+)/$', views.view_schilderij, name='view_schilderij'),
    url(r'^view_all/$', views.view_all, name='view_all'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_schilderij, name='edit_schilderij'),
    url('^login/$',auth_views.LoginView.as_view(template_name='photomgr/login.html', 
    	extra_context={'next':'/'}), name='login'),
]

'''
url('^change-password/$',auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
'''