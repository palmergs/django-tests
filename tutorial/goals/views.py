from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect

from .models import Goal
from .forms import GoalForm

def index(request):
	goals = Goal.objects.all()
	template = loader.get_template('goals/index.html')
	context = { 'goals': goals }
	return render(request, 'goals/index.html', context)


def goal_new(request):
	if request.method == "POST":
		form = GoalForm(request.POST)
		if form.is_valid():
			goal = form.save(commit=False)
			goal.save()
		return redirect('goals:goal_show', goal_id=goal.pk)	
	else:
		form = GoalForm()
		return render(request, 'goals/goal_edit.html', { 'form': form })


def show(request, goal_id):
	goal = get_object_or_404(Goal, pk=goal_id)
	return render(request, 'goals/show.html', { 'goal' : goal })


def update(request, goal_id):
	return HttpResponse("The goal is %s." % goal_id)


def complete(request, goal_id):
	goal = get_object_or_404(Goal, pk=goal_id)
	msg = 'unchanged'
	if goal.completed():
		goal.completed_at = None
		goal.save()
		msg = 'not completed'
	elif goal.prerequisites_completed():
		goal.completed_at = timezone.now()
		goal.save()
		msg = 'completed'
	
	return HttpResponse("The goal is %s." % msg)


			
