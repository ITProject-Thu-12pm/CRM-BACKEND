"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contact import views
from user import user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.contact_list, name='contact-list'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact-detail'),
    path('user/<str:email>/', user_views.retrieve_user_by_email, name='retrieve_user_by_email'),
    # path('user/<int:pk>/', user_views.update_user_profile, name='update_user_profile'),
    path('user/', user_views.create_user, name='create_user'),
    path('login/', user_views.user_login, name = 'user_login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
