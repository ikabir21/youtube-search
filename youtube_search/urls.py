from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def indexView(request):
    return redirect("api/v1")

urlpatterns = [
    path('', indexView),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]
