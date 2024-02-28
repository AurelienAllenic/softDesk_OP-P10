# Dans models.py
from django.db import models
from django.conf import settings
from api_user.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Contributor(models.Model):

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project_id', 'user_id')

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)  # Exemple: Open, Closed, In Progress, etc.
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'title')  # Assure que le titre est unique par projet

    def __str__(self):
        return self.title


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    commenter = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.user_id.username} on {self.issue.title}"


