from classes import *
#Making first school and naming it
school = School()
school.adding_name()
#Lists
all_teachers_list = []
all_students_list = []
#Creating bunch of teachers and adding them to school
for i in range(5):
    teacher = Teacher()
    teacher.naming_teachers()
    school.adding_teacher(teacher)
    all_teachers_list.append(teacher)
#Creating bunch of student
for i in range(10):
    student = Student()
    student.naming_student()
    all_students_list.append(student)
#Creating second school
school2 = School()
school2.adding_name()
#Adding all the students to the first school
for i in all_students_list:
    school.registering_student_2school(i)
#Trying to add all the students into the second school
for i in all_students_list:
    school2.registering_student_2school(i)
#Checking if adding all the students into the second school failed or not
if school2.students.__len__() == 0:
    print(f"The second school could not register students to the second school")
#Creating different subjects and adding them to school and adding teachers who teach the subject
#First Subject
pe = Subject()
pe.naming_subject("pe")
school.adding_subject(pe)
pe.adding_teacher(school.teacher[0])
pe.adding_teacher(school.teacher[1])
pe.adding_teacher(school.teacher[2])
#Second Subject
it = Subject()
it.naming_subject("it")
school.adding_subject(it)
it.adding_teacher(school.teacher[3])
#Third Subject
cooking_class = Subject()
cooking_class.naming_subject("cooking class")
school.adding_subject(cooking_class)
cooking_class.adding_teacher(school.teacher[4])
#Creating different grades where people could study
itdeveloper = Grade()
itdeveloper.naming_grade("IT Developer")
school.adding_grades(itdeveloper)
chef = Grade()
chef.naming_grade("Chef")
school.adding_grades(chef)
#Adding subject that the x grade has to learn
pe.add_grade_to_subject(itdeveloper)
pe.add_grade_to_subject(chef)
it.add_grade_to_subject(itdeveloper)
cooking_class.add_grade_to_subject(chef)
#Adding students to their grades
b = 0
for i in school.students:
    if b < 5:
        i.adding_grade(itdeveloper)
    if b >= 5:
        i.adding_grade(chef)
    b = b + 1
#Students registering to subjects
for i in itdeveloper.students:
    i.registering_to_subject(it)
    i.registering_to_subject(pe)
for i in chef.students:
    i.registering_to_subject(cooking_class)
    i.registering_to_subject(pe)
#Students getting marks/grades for subjects
c = 0
for i in itdeveloper.students:
    if c == 0:
        i.add_a_mark(1, it)
        i.add_a_mark(2, pe)
    if c == 1:
        i.add_a_mark(3, it)
        i.add_a_mark(4, pe)
    if c == 5:
        i.add_a_mark(5, it)
        i.add_a_mark(5, pe)
    elif c > 1:
        i.add_a_mark(3, it)
        i.add_a_mark(3, pe)
    c = c + 1
d = 0
for i in chef.students:
    if d == 0:
        i.add_a_mark(1, cooking_class)
        i.add_a_mark(2,pe)
    if d == 1:
        i.add_a_mark(3, cooking_class)
        i.add_a_mark(4,pe)
    if d == 5:
        i.add_a_mark(5, cooking_class)
        i.add_a_mark(5, pe)
    elif d > 1:
        i.add_a_mark(3, cooking_class)
        i.add_a_mark(3, pe)
    d = d + 1
#Checking the students subject status
for i in itdeveloper.students:
    i.show_subject_stats()
for i in chef.students:
    i.show_subject_stats()
#Showing teacher, student and subject lists
school.show_grades()
school.show_teacher()
school.show_subject()
school.show_students()
#Showing what teacher teaches what
for i in school.teacher:
    i.show_subjects()
#Show school ranking
school.show_school_ranking(school, school.students)