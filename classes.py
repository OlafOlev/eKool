class School:
    name = ""
    grade = []
    subject = []
    def adding_name(self):
        self.name = input("Name the school:")
    def adding_grades(self,grade):
        self.grade.append(grade.name)
    def adding_subject(self,subject):
        self.subject.append(subject.name)
class Grade:
    name = ""
    def naming_grade(self):
        self.name = input(str("Enter grade name:"))
class Subject:
    name = ""
    required_to_study = []
    def naming_subject(self):
        self.name = input(str("Enter subject name:"))
    def add_grade_to_subject(self,grade):
        self.required_to_study.append(grade)