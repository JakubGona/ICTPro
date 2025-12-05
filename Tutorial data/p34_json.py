import json

students = [
    {'name': 'Adam', 'surname': 'Bernau', 'age': 12},
    {'name': 'Bára', 'surname': 'Louková', 'age': 15},
    {'name': 'Cecil', 'surname': 'Novák', 'age': 17}
]

for student in students:
    print(f"{student['name']} {student['surname']} {student['age']}")

try:
    with open("students.json", "w", encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(e)

print("="*80)

try:
    with open("students.json", 'r', encoding='utf-8') as f:
        students_new = json.load(f)
        for student in students_new:
            print(student)
except Exception as e:
    print(e)


