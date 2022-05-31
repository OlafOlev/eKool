class School:
    def __init__(self):
        self.name = ""
        self.grade = []
        self.subject = []
        self.teacher = []
        self.students = []
        self.ranked_students = []
    def adding_name(self):
        self.name = input("Name the school:")
    def adding_grades(self, grade):
        self.grade.append(grade)
    def adding_subject(self, subject):
        self.subject.append(subject)
    def adding_teacher(self, teacher):
        self.teacher.append(teacher)
        teacher.teaching_school(self)
    def registering_student_2school(self, student):
        if student.student_school == "":
            self.students.append(student)
            student.student_school = self
    def show_grades(self):
        print("---" + f"This is grade school list")
        for i in self.grade:
            print(i.name)
    def show_students(self):
        print("---" + f"This is student school list")
        for i in self.students:
            print(i.student_name)
    def show_teacher(self):
        print("---" + f"This is teacher school list")
        for i in self.teacher:
            print(i.name)
    def show_subject(self):
        print("---" + f"This is subject school list")
        for i in self.subject:
            print(i.name)
    def getmark(self, student):
        return student.return_avg_mark()
    def getranked(self, students, school):
        for i in students:
            i.getting_avg_mark(i)
        self.ranked_students = sorted(students, key=school.getmark, reverse=True)
    def show_school_ranking(self, school, students):
        print("---" + f"School student ranking:")
        self.getranked(students, school)
        g = 1
        for i in self.ranked_students:
            print(str(g) + ".", i.student_name,f"average grade is ", str(i.student_avg_mark))
            g += 1
class Grade:
    def __init__(self):
        self.name = ""
        self.students = []
        self.grade_required_to_study = []
    def naming_grade(self, name):
        self.name = name
    def students_learning_the_grade(self, student):
        self.students.append(student)
    def add_subject_to_grade(self, subject):
        self.grade_required_to_study.append(subject)
class Subject:
    def __init__(self):
        self.name = ""
        self.required_to_study = []
        self.teacher = []
        self.students = []
    def naming_subject(self, name):
        self.name = name
    def add_grade_to_subject(self, grade):
        self.required_to_study.append(grade)
        grade.add_subject_to_grade(self)
    def adding_teacher(self, teacher):
        self.teacher.append(teacher)
        teacher.teaching_subjects(self)
    def registering_student_2subject(self, student, subject):
        for i in subject.required_to_study:
            if i == student.student_grade:
                subject.students.append(student)
                student.adding_subject(student)
            else:
                print("---" + "You cant study this")
class Teacher:
    def __init__(self):
        self.name = ""
        self.schools = []
        self.subjects = []
    def naming_teachers(self):
        self.name = input(str("Enter teacher name:"))
    def teaching_subjects(self, subject):
        self.subjects.append(subject)
    def teaching_school(self, school):
        self.schools.append(school)
    def show_subjects(self):
        print("---" + self.name, f"teaches these subjects")
        for i in self.subjects:
            print(i.name)
class Student:
    def __init__(self):
        self.student_school = ""
        self.student_avg_mark = 0
        self.student_name = ""
        self.student_grade = ""
        self.student_marks = [] #grade as "You got 2 on your test"
        self.student_mark_total = 0
        self.student_subjects = []
        self.failed_subjects = []
        self.passed_subjects = []
        self.student_required_to_study = []
    def return_avg_mark(self):
        return self.student_avg_mark
    def getting_avg_mark(self, student):
        for i in student.student_marks:
            self.student_mark_total += i
        self.student_avg_mark = round(self.student_mark_total/len(self.student_marks),2)
        return student.student_avg_mark
    def naming_student(self):
        self.student_name = input(str("Enter student name:"))
    def  registering_to_subject(self, subject):
        for i in self.student_required_to_study:
            if i == subject:
                self.student_subjects.append(subject)
    def adding_grade(self, grade):
        self.student_grade = grade
        self.student_required_to_study = grade.grade_required_to_study
        grade.students_learning_the_grade(self)
    def passed_the_subject(self, subject):
        self.passed_subjects.append(subject)
    def failed_the_subject(self, subject):
        self.failed_subjects.append(subject)
    def add_a_mark(self, mark, subject):
        if mark == 1 or mark == 2 or mark == 3 or mark == 4 or mark == 5:
            self.student_marks.append(mark)
            if mark == 1 or mark == 2:
                self.failed_the_subject(subject)
            if mark == 3 or mark == 4 or mark == 5:
                self.passed_the_subject(subject)
    def show_subject_stats(self):
        print("---" + self.student_name, f"subject status is:")
        if self.failed_subjects.__len__() == 0:
            print(f"---No failed subjects")
        else:
            print(f"---Failed subjects:")
            for i in self.failed_subjects:
                print(i.name)
        if self.passed_subjects.__len__() == 0:
            print(f"---No passed subjects")
        else:
            print(f"---Passed subjects:")
            for i in self.passed_subjects:
                print(i.name)