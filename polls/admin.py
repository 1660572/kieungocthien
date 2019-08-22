from django.contrib import admin
 
# Register your models here.
from .models import Question, Choice
 
class ChoiceInLine(admin.TabularInline):
    model = Choice 
    extra = 2
  
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    
    list_display = ('choice_text', 'votes','question')
    list_filter = ['votes']
    search_fields = ['choice_text']
 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)