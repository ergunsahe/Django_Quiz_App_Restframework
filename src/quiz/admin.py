from django.contrib import admin
from .models import Category, Question, Quiz, Answer
import nested_admin

class AnswerInline(nested_admin.NestedTabularInline): # this prepare Answer table as a inline/nested table
    model = Answer
    extra = 4
    max_num = 8
    
class QuestionInline(nested_admin.NestedTabularInline): # this make a table Question and answer table together
    model = Question
    inlines = [AnswerInline]
    extra = 1
    max_number = 10
    
class QuizAdmin(nested_admin.NestedModelAdmin): #this is like an end point to make table to display quiz and nested question table together so we use nested model admin
    model = Quiz
    inlines = [QuestionInline]
    

admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
