class School:
    name = ""
    grade = []
    def adding_name(self):
        self.name = input("Name the school:")
    def adding_grades(self,grade):
        self.grade.append(grade)
class Grade:
    name = ""
    def naming_grade(self):
        self.name = input(str("Enter grade name:"))