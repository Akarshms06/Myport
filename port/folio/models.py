from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True)
    project_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
