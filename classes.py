class School:
    name = ""
    grade = []
    subject = []
    teacher = []
    students = []
    def adding_name(self):
        self.name = input("Name the school:")
    def adding_grades(self,grade):
        self.grade.append(grade.name)
    def adding_subject(self,subject):
        self.subject.append(subject.name)
    def adding_teacher(self,teacher):
        self.teacher.append(teacher.name)
    def registering_student_2school(self, student):
        self.students.append(student.student_name)
    def show_grades(self):
        return self.grade
    def show_students(self):
        return self.students
    def show_teacher(self):
        return self.teacher
    def show_subject(self):
        return self.subject
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
    name = ""
    students = []
    def naming_grade(self):
        self.name = input(str("Enter grade name:"))
    def students_learning_thegrade(self, student):
        self.students.append(student)
        student.adding_grade(self.name)
class Subject:
    name = ""
    required_to_study = []
    teacher = []
    students = []
    def naming_subject(self):
        self.name = input(str("Enter subject name:"))
    def add_grade_to_subject(self,grade):
        self.required_to_study.append(grade.name)
    def adding_teacher(self, teacher):
        self.teacher.append(teacher.name)
    def registering_student_2subject(self,student):
        for i in self.required_to_study:
            if i == student.student_grade:
                self.students.append(student.student_name)
                student.adding_subject(self.name)
            else:
                print("You cant study this")
class Teacher:
    name = ""
    schools = []
    subjects = []
    def naming_teachers(self):
        self.name = input(str("Enter teacher name:"))
    def teaching_subjects(self, subject):
        self.subjects.append(subject.name)
    def teaching_school(self, school):
        self.schools.append(school.name)
class Student:
    student_name = ""
    student_grade = ""
    student_marks = [] #grade as "You got 2 on your test"
    student_avg_mark = 0
    student_mark_total = 0
    def getting_avg_mark(self):
        for i in self.student_marks:
            self.student_mark_total += i
        self.student_avg_mark = round(self.student_mark_total/len(self.student_marks),2)
        return self.student_avg_mark
    student_subjects = []
    failed_subjects = []
    passed_subjects = []
    def naming_student(self):
        self.student_name = input(str("Enter student name:"))
    def adding_subject(self, subject):
        self.student_subjects.append(subject)
    def adding_grade(self, grade):
        self.student_grade = grade
    def passed_the_subject(self, subject):
        self.passed_subjects.append(subject.name)
    def failed_the_subject(self, subject):
        self.failed_subjects.append(subject.name)
    def add_a_mark(self, mark):
        self.student_marks.append(mark)