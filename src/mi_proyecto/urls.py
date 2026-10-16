from django.contrib import admin
from django.urls import path
from mi_app.views import vista_suma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista_suma, name='suma'),
]