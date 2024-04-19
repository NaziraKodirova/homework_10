from django.urls import path
from .views import CourseListView, TeacherListView, CourseDetailView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('course/',CourseListView.as_view(), name='courses'),
    path('teachers/',TeacherListView.as_view(), name='teachers'),
    path('course/<int:id>/',CourseDetailView.as_view(), name='course-detail'),
    path('update/<int:id>/',CourseUpdateView.as_view(), name='course-update'),
    path('delete/<int:id>/',CourseDeleteView.as_view(), name='course-delete'),
]