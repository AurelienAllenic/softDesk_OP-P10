from django.contrib import admin
from django.urls import path
from api_user.views import CustomUserList, CustomUserDetail, MyTokenObtainPairView
from api_project.views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView, ContributorListCreateAPIView, ContributorRetrieveUpdateDestroyAPIView, IssueListCreateAPIView, IssueRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', CustomUserList.as_view(), name='customuser-list'),
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='customuser-detail'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
    path('contributors/', ContributorListCreateAPIView.as_view(), name='contributor-list'),
    path('contributors/<int:pk>/', ContributorRetrieveUpdateDestroyAPIView.as_view(), name='contributor-detail'),
    path('issues/', IssueListCreateAPIView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>/', IssueRetrieveUpdateDestroyAPIView.as_view(), name='issue-detail'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]
