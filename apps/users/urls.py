from django.urls import path
from .views import UserDetailView
urlpatterns = [
    path('detail/', UserDetailView.as_view(), name='user-detail')
]
