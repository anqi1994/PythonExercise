class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrollments = []


class Course:
    def __init__(self, coursename, coursecode, instructors):
        self.coursename = coursename
        self.coursecode = coursecode
        self.instructors = instructors
        self.enrollments = []


class Enrollment:
    def __init__(self, student, course, progress=0.0):
        self.student = student
        self.course = course
        self.progress = progress


def enroll(student, course):
    enrollment = Enrollment(student, course)
    student.enrollments.append(enrollment)
    course.enrollments.append(enrollment)


def update_progress(student, course, progress):
    for enrollment in student.enrollments:
        if enrollment.course == course:
            enrollment.progress = progress


def print_student_enrollment(student):
    print(f"Student ID: {student.student_id}\n"
          f"Student Name: {student.name}\n"
          f"Enrollments:")
    for enrollment in student.enrollments:
        print(f"Course: {enrollment.course.coursename}\n"
              f"Course Code: {enrollment.course.coursecode}\n"
              f"Progress: {enrollment.progress}\n"
              f"Instructors: ", ", ".join(enrollment.course.instructors))


student1 = Student(1, "Timo")
student2 = Student(2, "Amy")

course1 = Course("CS101", "Introduction", ["A"])
course2 = Course("CS102", "Physics", ["B"])
course3 = Course("CS103", "Math", ["A", "B"])

enroll(student1, course1)
enroll(student1, course2)
enroll(student1, course3)
enroll(student2, course2)

update_progress(student1, course1, 75.0)
update_progress(student2, course2, 85.5)
update_progress(student1, course2, 35.6)

print_student_enrollment(student1)

print(course1.enrollments)
