
from django.urls import path
from .views import StudentListAPIView, StudentRetrieveAPIView

urlpatterns = [
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<str:pk>/', StudentRetrieveAPIView.as_view(), name='student-detail'),
]