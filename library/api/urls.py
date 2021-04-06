from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='v1/')),
    path('v1/', include('api.v1.urls'), name='api_v1'),
]