from django.contrib import admin
from django.urls import path,include
from .api import router

urlpatterns =[

	path('admin/', admin.site.urls),
    #My New App
	path('', include('ListExam.urls')),
	path('accounts/', include('allauth.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
    #new one
	path('api-auth/', include('rest_framework.urls')),

	path('api/v1/', include(router.urls)),
    ]
