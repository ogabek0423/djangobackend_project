from django.urls import path
from .views import BookListView, BookDetailView, CourseListView, TeacherList
from .views import About, Blog, ContactView, NotesView, SinglePageView


urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:id>/', BookDetailView.as_view(), name='a_detail'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('teachers/', TeacherList.as_view(), name='teachers'),
    path('about/', About.as_view(), name='about'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('notes/', NotesView.as_view(), name='notes'),
    path('singlepage/', SinglePageView.as_view(), name='singlepage'),


]