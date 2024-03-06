# Dans models.py
from django.db import models
from django.conf import settings
from api_user.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)

class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user')

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    class Meta:
        unique_together = ('project', 'title')

    def __str__(self):
        return self.title

def get_default_project_id():
    first_project = Project.objects.first()
    return first_project.id if first_project else None

class Comment(models.Model):
    title = models.CharField(max_length=100, default="")  # Défaut à une chaîne vide
    description = models.TextField(default="")  # Défaut à une chaîne vide
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=get_default_project_id)  # Défaut à l'ID du premier projet
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)  # Peut être laissé vide

    def __str__(self):
        return self.title


@receiver(post_save, sender=Issue)
def create_issue_contributor(sender, instance, created, **kwargs):
    if created and instance.created_by and instance.project:
        Contributor.objects.get_or_create(user=instance.created_by, project=instance.project)

@receiver(post_save, sender=Comment)
def create_comment_contributor(sender, instance, created, **kwargs):
    if created and instance.created_by and instance.project:
        Contributor.objects.get_or_create(user=instance.created_by, project=instance.project)



