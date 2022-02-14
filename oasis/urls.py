
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='register/')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('register/', include('register.urls'))
]
