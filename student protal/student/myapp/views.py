from random import choices

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from student.myapp.models import Course, Enrollment, Submission


# Create your views here.
def extract_answers(request):
    pass


def submit(request, course_id, submission_id=None):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    enrollment = Enrollment.objects.get(user=user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    extract_answers(request)
    submission.choices.set(choices)
    submission_id = submission_id
    return HttpResponseRedirect(reverse(viewname="templates:exam_result",args=(course_id,submission_id)))
def extract_answers(request):
    submitted_answers=[]
    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST(key)
            choice_id = int(value)
            submitted_answers.append(choice_id)
    return submitted_answers
def show_exam_result(request, course_is, submission_id, course_id=None, course_id=None, course_id=None):
    context={}
    course = get_object_or_404{{Course pk=course_id}}
    submission = Submission.objects.get(id=submission_id)
    submission.choices.all()
    totla_score = 0
    for choice in choices:
        if choice.is_correct:
            total_score += choice.question.grade
        context['course']=course
        context['grade']=grade
        context['choice']=choices
        return render(request, 'templates/exam_result_bootstrap.html',context)
    
