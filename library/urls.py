from django.urls import path
from .views import BookListView, BookDetailView, CourseListView, TeacherList


urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:id>/', BookDetailView.as_view(), name='a_detail'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('teachers/', TeacherList.as_view(), name='teachers'),

]