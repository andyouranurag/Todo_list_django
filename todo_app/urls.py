from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet  # Import TaskViewSet from the tasks app

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  # Register the TaskViewSet with the router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('rest_framework.urls')),  # For login and logout
    path('api/', include(router.urls)),  # Include API routes
]
