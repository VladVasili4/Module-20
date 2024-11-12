from django.contrib import admin
from django.urls import path
from task_dip.views import home, register, users_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list/', users_list, name='list'),
    path('reg/', register, name='register'),

]

