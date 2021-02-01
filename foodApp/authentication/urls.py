from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi
from .views import ApiViewHome, ApiView

urlpatterns = [
      path('api/register/', RegisterApi.as_view()),
	  path('', ApiViewHome.as_view()),
	  path('api/', ApiView.as_view()),
]