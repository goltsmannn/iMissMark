from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'wishes', views.WishViewSet)

urlpatterns = [
    path('', include(router.urls))
  #  path('  ', views.index, name='index'),
]