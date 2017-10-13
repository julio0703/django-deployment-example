from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

app_name = 'firstApp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^contact/$',views.contact_page,name='contact'),
    url(r'^escorts/$',views.EscortListView.as_view(),name='escort_list'),
    url(r'^escort/(?P<pk>\d+)/$',views.DetailEscortView.as_view(),name='escort_detail'),
    url(r'^escort/(?P<pk>\d+)/edit/$',views.UpdateExcortView.as_view(),name='escort_edit'),
    url(r'^escort/(?P<pk>\d+)/remove/$',views.DeleteEscortView.as_view(),name='escort_delete'),
    url(r'^create/$',views.CreateEscortView.as_view(),name='escort_form'),
    url(r'^login/$',auth_views.login, name='login'),
    url(r'^logout/$',auth_views.logout, {'next_page':'/'},name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
