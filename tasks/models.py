from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    due_date = models.DateTimeField(editable=True)
    completed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)
    owner = models.ForeignKey('auth.User',related_name='tasks',on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['updated']
