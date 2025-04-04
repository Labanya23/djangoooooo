"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .import views
app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='',view=views.CourseListView.as_view(), name='index'),
    path('registration/',views.registration_request,name='registration'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('<int:pk>/',views.CourseDetailView.as_view(),name='course_details'),
    path('<int:course_id>/enroll/',views.enroll,name="submit"),
    path('<course/int:course_id>/submission/<int:submission_id>result/',views.show_exam_result,name="exam_result"),
]+static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
