from group import Group
from student import Student
from excess import ExcessNumberOfStudents

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student("Male", 61, "Michael", "Jordan", "NBA148")
st4 = Student("Male", 48, "Andrey", "Shevchenko", "Football010")
st5 = Student("Male", 43, "Roger", "Federer", "Tennis225")
st6 = Student('Male', 30, 'Steve1', 'Jobs1', 'AN1421')
st7 = Student('Female', 25, 'Liza1', 'Taylor1', 'AN1451')
st8 = Student("Male", 61, "Michael1", "Jordan1", "NBA1481")
st9 = Student("Male", 48, "Andrey1", "Shevchenko1", "Football0101")
st10 = Student("Male", 43, "Roger1", "Federer1", "Tennis2251")
st11 = Student("Male", 35, "Mister", "Excess", "none")
gr = Group("Famous", 10)

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except ExcessNumberOfStudents as error:
    print(f"error {error}")

print(gr)
assert gr.find_student("Jobs") == st1
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student


