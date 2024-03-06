from rest_framework import serializers
from .models import Contributor, Project, Issue, Comment
from rest_framework.serializers import ModelSerializer


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project_id']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
