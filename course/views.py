from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher

class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            "courses": courses
        }
        return render(request, 'main/course.html', context)
    
    
class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            "teachers": teachers
        }
        return render(request, 'main/teacher.html', context)
    

class CourseDetailView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request,"main/course_detail.html",{'course': course})
    
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('courses')
    

class CourseUpdateView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'main/course_update.html',{'course': course})
    

    def post(self, request, id):
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')

        course = Course.objects.get(id=id)
        course.title = new_title
        course.description = new_description
        course.price = new_price
        course.save()

        return redirect('courses')
    



class CourseDeleteView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('courses')