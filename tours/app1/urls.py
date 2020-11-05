from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('edit', views.edit, name='edit'),
    path('book', views.book, name='book'),
    path('browse', views.browse, name='browse'),
    path('package/<int:p_id>',views.package,name='package')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
