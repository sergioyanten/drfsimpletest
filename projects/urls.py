from rest_framework import routers
from .api import ProjectViewSet

router=routers.DefaultRouter()

router.register('api/project',ProjectViewSet,'projects')

urlpatterns =router.urls