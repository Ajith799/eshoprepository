from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test1/',views.test,name='test1')
]