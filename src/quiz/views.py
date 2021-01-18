from django.shortcuts import render
from rest_framework import generics
from .models import Category, Question, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
    

class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]
    
    
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs["category"]
        queryset = queryset.filter(category__name= category)
        
        return queryset


class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title)
        
        return queryset