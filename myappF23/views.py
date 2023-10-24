from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Course, Student, Instructor, Order


# Existing index view
def index(request):
    # Get a list of up to 10 categories
    category_list = Category.objects.all().order_by('id')[:10]

    # Update the query to get up to 5 courses sorted by price in descending order
    courses = Course.objects.order_by('-price')[:5]

    # Get all students, instructors, and orders
    students = Student.objects.all()
    instructors = Instructor.objects.all()
    orders = Order.objects.all()

    context = {
        'category_list': category_list,
        'categories': category_list,  # You can use both 'category_list' and 'categories' in your template
        'courses': courses,
        'students': students,
        'instructors': instructors,
        'orders': orders,
    }

    return render(request, 'myappF23/index.html', context)

# New about view
def about(request):
    message = "This is a Distance Education Website! Search our Categories to find all available Courses."
    context = {'message': message}
    return render(request, 'myappF23/about.html', context)



def detail(request, category_no):
    # Get the category based on the category_no or return a 404 error if it doesn't exist
    category = get_object_or_404(Category, pk=category_no)

    # Get a list of courses for the specified category
    courses = Course.objects.filter(categories=category)

    context = {
        'category': category,
        'courses': courses,
    }

    return render(request, 'myappF23/detail.html', context)

