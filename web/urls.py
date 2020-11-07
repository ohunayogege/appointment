from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import MakeAppointmentView
# from .views import MakeAppointment

router = DefaultRouter()
router.register(r'appointments', MakeAppointmentView, basename='appointment')

urlpatterns = [
    # url(r'appointments/', MakeAppointment.as_view(), name='make-appointment'),
    # url(r'appointments/<int:pk>/', MakeAppointment.as_view(), name='update-appointment'),
    url(r'api/', include(router.urls)),
]
