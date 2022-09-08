from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('authentication.urls', 'authentication'), namespace='authentication')),
    path('players/', include(('players.urls', 'players'), namespace='players')),
]
