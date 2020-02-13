from brightwheelemail import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'send_email', views.EmailViewSet, basename='send_email')

urlpatterns = router.urls
