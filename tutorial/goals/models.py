from django.core.exceptions import ValidationError
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


    def save(self, **kwargs):
        self.clean()
        return super(Prereq, self).save(**kwargs)


    def clean(self):
        left_arr = [ self.prereq ]
        right_arr = [ self.postreq ]
        for goal in left_arr:
            for p in goal.prerequisites.all():
                if p.prereq in right_arr:
                    raise ValidationError('Prereq found in post-requisite list')
                left_arr.append(p.prereq)
                print(len(left_arr))
        for goal in right_arr:
            for p in goal.dependents.all():
                if p.postreq in left_arr:
                    raise ValidationError('Post-requisite found in prereq list')
                right_arr.append(p.postreq)
                print(len(right_arr))
        



        
