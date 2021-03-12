from django.urls import path, include
from pages.views import AboutView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
]
