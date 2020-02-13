from brightwheelemail import views
from django import urls

urlpatterns = [
    urls.path('send_email/', views.EmailViewSet.as_view(),
              name='send_email')
]
