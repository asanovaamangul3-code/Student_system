from students import add_student, show_students, students
from search import search_student

add_student("Иванов Иван")
add_student("Петров Петр")

show_students()

result = search_student("Иванов Иван", students)

if result:
    print("Найден:", result)
else:
    print("Студент не найден")
