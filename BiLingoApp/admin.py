from pyexpat import model
from django.contrib import admin
from .models import Answer, Category, Destination,Profile, Question

# Register your models here.


admin.site.register(Profile)


admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines =[AnswerAdmin]

admin.site.register(Question , QuestionAdmin)
admin.site.register(Answer)