from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer
from .serializers import ContributorSerializer
from .serializers import IssueSerializer
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from api_user.permissions import IsObjectOwnerOrReadOnly, IsSuperuserOrReadOnly


class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsObjectOwnerOrReadOnly]


class ContributorListCreateAPIView(ListCreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]


class ContributorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsSuperuserOrReadOnly, IsAuthenticated]


class IssueListCreateAPIView(ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(created_by=user)


class IssueRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
                            IsAuthenticated,
                            IsObjectOwnerOrReadOnly | IsSuperuserOrReadOnly
                        ]


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(created_by=user)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
                            IsAuthenticated,
                            IsObjectOwnerOrReadOnly | IsSuperuserOrReadOnly
                        ]

    def perform_update(self, serializer):
        user = self.request.user

        serializer.save(created_by=user)
