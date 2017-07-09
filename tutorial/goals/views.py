from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.shortcuts import render

from .models import Goal

def index(request):
	goals = Goal.objects.all()
	template = loader.get_template('goals/index.html')
	context = { 'goals': goals }
	return render(request, 'goals/index.html', context)


def show(request, goal_id):
	return HttpResponse("You're looking at goal %s." % goal_id)


def complete(request, goal_id):
	goal = Goal.objects.get(id=goal_id)
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


			
