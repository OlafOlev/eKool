from classes import *
school = School()
grade = Grade()
subject_proge = Subject()
teacher = Teacher()
school.adding_name()
grade.naming_grade()
teacher.naming_teachers()
student = Student()
student.naming_student()
school.adding_grades(grade)
school.adding_teacher(teacher)
subject_proge.naming_subject()
subject_proge.add_grade_to_subject(grade)
school.adding_subject(subject_proge)
subject_proge.adding_teacher(teacher)
teacher.teaching_subjects(subject_proge)
teacher.teaching_school(school)
school.registering_student_2school(student)
grade.students_learning_thegrade(student)
subject_proge.registering_student_2subject(student)
print(school.name)
print(grade.name)
print(school.grade)
print(school.subject)
print(school.teacher)
print(school.students)
print(subject_proge.name)
print(subject_proge.teacher)
print(subject_proge.required_to_study)
print(subject_proge.students)
print(teacher.name)
print(teacher.schools)
print(teacher.subjects)
print(student.student_name)
print(student.student_grade)
print(student.student_subjects)