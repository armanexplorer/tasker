from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'tasks.views.Custom404'
# handler500 = 'tasks.views.Custom500'
