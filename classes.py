class School:
    name = ""
    grade = []
    subject = []
    teacher = []
    def adding_name(self):
        self.name = input("Name the school:")
    def adding_grades(self,grade):
        self.grade.append(grade.name)
    def adding_subject(self,subject):
        self.subject.append(subject.name)
    def adding_teacher(self,teacher):
        self.teacher.append(teacher.name)
class Grade:
    name = ""
    def naming_grade(self):
        self.name = input(str("Enter grade name:"))
class Subject:
    name = ""
    required_to_study = []
    teacher = []
    def naming_subject(self):
        self.name = input(str("Enter subject name:"))
    def add_grade_to_subject(self,grade):
        self.required_to_study.append(grade.name)
    def adding_teacher(self, teacher):
        self.teacher.append(teacher.name)
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