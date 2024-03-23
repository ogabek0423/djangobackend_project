from django.shortcuts import render
from django.views import View
from library.models import CoursesRecord, CourseSpeciality


class LandingPageView(View):
    def get(self, request):
        context = {'courses': CoursesRecord.objects.all(),
                   'specs': CourseSpeciality.objects.all()}
        return render(request, 'landing_page.html', context)




