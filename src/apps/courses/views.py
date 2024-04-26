from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Course
from .forms import CourseForm

# #/products->index
# def index(request):
#     return HttpResponse("Hello,world")


# def is_manager(user):
#     return user.groups.filter(name='Manager').exists()


# @login_required
# @user_passes_test(is_manager)
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


# @login_required
# @user_passes_test(is_manager)
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    print("Course object:", course)
    print("Form data:", request.POST)
    print("Files:", request.FILES)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)# Pass request.FILES here
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'update_course.html', {'form': form})




# def course_update(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#
#     if request.method == 'POST':
#         form = CourseForm(request.POST, request.FILES, instance=course)  # Pass request.FILES here
#         if form.is_valid():
#             # Delete old files before saving new ones
#             if 'file' in form.changed_data and course.file:
#                 course.file.delete(save=False)
#             if 'video' in form.changed_data and course.video:
#                 course.video.delete(save=False)
#
#             form.save()
#             return redirect('course_list')
#     else:
#         form = CourseForm(instance=course)
#
#     return render(request, 'update_course.html', {'form': form})



@login_required
def course_list(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'course_list.html', {'page_obj': page_obj})


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})


# @login_required
# @user_passes_test(is_manager)
# def publish_course(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#
#     if request.method == 'POST':
#         if course.is_published:
#             course.is_published = False
#         else:
#             course.is_published = True
#             course.publish_date = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S') # Set the publish date
#
#         course.save()
#
#         # Redirect to the new page where only published courses are displayed
#         return redirect('published_course_list')
#
#     context = {'course': course}
#     return render(request, 'publish_confirm.html', context)


def publish_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        if not course.is_published:
            course.is_published = True
            course.publish_date = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S') # Set the publish date
            course.save()

        # Redirect to the page where only published courses are displayed
        return redirect('published_course_list')

    context = {'course': course}
    return render(request, 'publish_confirm.html', context)


def unpublish_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        if course.is_published:
            course.is_published = False
            course.save()

        # Render the current page again with all courses
        courses = Course.objects.all()
        paginator = Paginator(courses, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'course_list.html', {'page_obj': page_obj})

    context = {'course': course}
    return render(request, 'publish_confirm.html', context)

# @login_required
def published_course_list(request):
    published_courses = Course.objects.filter(is_published=True)
    paginator = Paginator(published_courses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'published_course_list.html', {'page_obj': page_obj})

def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    # return redirect('course_details')
    return render(request, 'course_details.html', {'course': course})
#
class Enrollment:
    objects = None


def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.create(user=request.user, course=course)
    return redirect('course_list')


def unenroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.filter(user=request.user, course=course).delete()
    return redirect('course_list')