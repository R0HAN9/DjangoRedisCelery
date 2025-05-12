from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, ReminderViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]