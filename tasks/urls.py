from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'tasks',views.TaskViewSet,basename='tasks')
router.register(r'users',views.UserViewSet,basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]