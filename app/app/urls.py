from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles import views
from django.conf.urls.static import static


urlpatterns = [
    path('', include('app.products.urls')),
    path('clients/', include('app.clients.urls')),
    path('invoices/', include('app.invoices.urls')),
    path('admin_v2/', admin.site.urls),
] 
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]