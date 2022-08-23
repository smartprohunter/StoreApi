
from django.contrib import admin
from django.urls import path, include

from StoreApi.schema import schema_view

urlpatterns = [
    path('', schema_view, name='schema'),

    path('admin/', admin.site.urls),
    path('api/', include('StoreApi.api.urls'))
]
