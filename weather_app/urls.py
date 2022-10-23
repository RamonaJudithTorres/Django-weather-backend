from django.urls import include, path
from rest_framework import routers
from rest_api import views

router = routers.DefaultRouter()
router.register(r'weather', views.RecordViewSetWithOptions, basename='Record')

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]