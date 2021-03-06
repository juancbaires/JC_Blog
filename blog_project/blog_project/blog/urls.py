from django.conf.urls import url, include
from rest_framework import routers
from blog.views import views

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]