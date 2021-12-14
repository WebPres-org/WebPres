from filebrowser.sites import site

urlpatterns = patterns('',
   url(r'^adminurl/filebrowser/', include(site.urls)),
)