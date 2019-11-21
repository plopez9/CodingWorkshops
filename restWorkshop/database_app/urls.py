from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("Fires", views.FireView)

urlpatterns = [
    path("", include(router.urls)),
]
