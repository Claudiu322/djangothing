from django.contrib import admin
from .models import Question, Choice

class QuestionInfo(admin.ModelAdmin):
    list_display = ('question_text','pub_date')

class ChoiceInfo(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')

admin.site.register(Question, QuestionInfo)
admin.site.register(Choice, ChoiceInfo)