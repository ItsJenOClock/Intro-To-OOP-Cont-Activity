from school_schedule.student import Student
import pytest

# Write your tests here!
def test_student_initialization():
    name = "Jen Nguyen"
    grade = "freshman"
    classes = ["Geometry", "English", "US History"]
    
    student = Student(name, grade, classes)

    assert student.name == "Jen Nguyen"
    assert student.grade == "freshman"
    assert student.classes == ["Geometry", "English", "US History"]

def test_add_class_empty_classes_list():
    name = "Joe Anderson"
    grade = "senior"
    classes = []
    student = Student(name, grade, classes)

    student.add_class("Algebra")

    assert student.classes == ["Algebra"]

def test_student_add_class_method_adds_class_get_num_classes():
    student_name = "John Doe"
    student_grade = "freshmen"
    student_classes = ["Algebra", "Astronomy", "Spanish"]
    student = Student(student_name, student_grade, student_classes)
    student.add_class("Geometry")
    
    assert student.get_num_classes() == 4

def test_display_classes_summary():
    student_name = "John Doe"
    student_grade = "freshmen"
    student_classes = ["Algebra", "Astronomy", "Spanish"]
    student = Student(student_name, student_grade, student_classes)
    student.add_class("Geometry")
    
    class_schedule = student.display_classes()
    student_summary = student.summary()

    assert class_schedule == "Algebra, Astronomy, Spanish, Geometry"
    assert student_summary == (f"{student.name} is a {student.grade} "
            f"enrolled in {student.get_num_classes()} classes: "
            f"{student.display_classes()}")
