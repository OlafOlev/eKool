from classes import *
school = School()
grade = Grade()
subject_proge = Subject()
school.adding_name()
grade.naming_grade()
school.adding_grades(grade)
subject_proge.naming_subject()
subject_proge.add_grade_to_subject(grade)
school.adding_subject(subject_proge)
print(school.name)
print(grade.name)
print(school.grade)
print(school.subject)