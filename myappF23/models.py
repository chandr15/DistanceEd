from django.db import models


class Student(models.Model):
    # Choices for student status
    STUDENT_STATUS_CHOICES = [
        ('ER', 'Enrolled'),
        ('SP', 'Suspended'),
        ('GD', 'Graduated'),
    ]

    # Fields for the Student model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Unique email field
    date_of_birth = models.DateField()
    status = models.CharField(max_length=2, choices=STUDENT_STATUS_CHOICES, default='ER')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Instructor(models.Model):
    # Fields for the Instructor model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    courses = models.ManyToManyField('Course', blank=True, related_name="instructors")  # Unique related_name
    students = models.ManyToManyField(Student)  # Many-to-many relationship with Student

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    # Fields for the Category model
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    # Choices for course level
    COURSE_LEVEL_CHOICES = [
        ('BE', 'Beginner'),
        ('IN', 'Intermediate'),
        ('AD', 'Advanced'),
    ]

    # Fields for the Course model
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)  # One-to-many relationship with Instructor
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=2, choices=COURSE_LEVEL_CHOICES)  # Choices for course level

    def __str__(self):
        return self.title


class Order(models.Model):
    COURSE_STATUS_CHOICES = (
        (0, 'Order Confirmed'),
        (1, 'Order Cancelled'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    order_status = models.IntegerField(choices=COURSE_STATUS_CHOICES, default=1)
    order_date = models.DateField()

    def __str__(self):
        return f"Order for {self.course} by {self.student}"
