from excess import ExcessNumberOfStudents
class Group:

    def __init__(self, name, students_limit = 4):
        self.name = name
        self.group = set()
        self.students_limit = students_limit

    def add_student(self, student):
        if len(self.group) == self.students_limit:
            raise ExcessNumberOfStudents(f"Number of students excess students limit {self.students_limit}",self.name)
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Number:{self.name}\n{all_students}'