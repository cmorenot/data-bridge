from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
from rest_framework.pagination import PageNumberPagination

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10  # Establece el número de estudiantes por página


class StudentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

