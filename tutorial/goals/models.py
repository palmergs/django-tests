from django.db import models
from django.utils import timezone

class Goal(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False, blank=True, default='')
    created_at = models.DateTimeField(null=False, default=timezone.now)
    completed_at = models.DateTimeField(null=True)

    def completed(self):
        return self.completed_at != None

class Prereq(models.Model):
    title = models.CharField(max_length=200, null=False, blank=True, default='')
    description = models.TextField(null=False, blank=True, default='')
    prereq = models.ForeignKey(Goal, null=False, on_delete=models.CASCADE, related_name='dependents')
    postreq = models.ForeignKey(Goal, null=False, on_delete=models.CASCADE, related_name='prerequisites')
    created_at = models.DateTimeField(null=False, default=timezone.now)

