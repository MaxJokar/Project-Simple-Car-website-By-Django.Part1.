"""
namespace= "blog" allows me to utilize these names like in reverse So ,I can refer to it as blog
"""

from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('blog.urls' , namespace= "blog"))# '' we use root directory

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




