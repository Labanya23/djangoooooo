from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'course', 'grade', 'created_at')
    list_filter = ['course', 'created_at']
    search_fields = ['content']


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ['course']
    search_fields = ['title']


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'enrollment', 'submission_date')
    list_filter = ['submission_date']
    filter_horizontal = ('choices',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
