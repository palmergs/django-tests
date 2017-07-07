from django.contrib import admin

from .models import Goal, Prereq

admin.site.register(Goal)
admin.site.register(Prereq)
