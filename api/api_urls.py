from django.conf.urls import url
from api.views import course
from api.views import degreecourse


urlpatterns = [
    url(r'courses/$', course.CoursesView.as_view()),
    url(r'courses/special/$', course.CoursesSpecialView.as_view()),
    url(r'courses/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),
    url(r'degreecourse/teachers/$', degreecourse.DegreeCourseTeacherView.as_view()),
    url(r'degreecourse/scholarship/$', degreecourse.DegreeCourseScholarshipView.as_view()),
    url(r'degreecourse/$', degreecourse.DegreeCourseView.as_view()),

    # url(r'degreecourse/(?P<pk>\d+)/$', degreecourse.DegreeCourseTeacherView()),
]