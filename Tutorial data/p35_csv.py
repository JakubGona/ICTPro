import csv

students = [
    {'name': 'Adam', 'surname': 'Bernau', 'age': 12},
    {'name': 'Bára', 'surname': 'Louková', 'age': 15},
    {'name': 'Cecil', 'surname': 'Novák', 'age': 17}
]

try:
    with open("students.csv", 'w', encoding='utf-8') as f:
        col_names = students[0].keys()
        i = 0
        for colname in col_names:
            f.write(colname)
            i += 1
            if i < len(col_names):
                f.write(";")
        f.write("\n")
        for student in students:
            i = 0
            for col_name in col_names:
                f.write(str(student[col_name]))
                i += 1
                if i < len(col_names):
                    f.write(";")
            f.write("\n")
except Exception as e:
    print(e)

print("="*80)

try:
    with open("students.csv", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip().split(";"))

except Exception as e:
    print(e)

print("="*80)
try:
    with open("students.csv", 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f, delimiter=";")
        for line in csv_file:
            print(line)
except Exception as e:
    print(e)

print("="*80)
try:
    with open("students.csv", 'r', encoding='utf-8') as f:
        csv_file = csv.DictReader(f, delimiter=";")
        for line in csv_file:
            print(line)
except Exception as e:
    print(e)

print("="*80)
students = [
    {'name': 'Adam', 'surname': 'Bernau', 'age': 12},
    {'name': 'Bára', 'surname': 'Louková', 'age': 15},
    {'name': 'Cecil', 'surname': 'Novák', 'age': 17}
]
print(students[0].keys())
try:
    with open("students2.csv", 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, delimiter=";", fieldnames=students[0].keys())
        writer.writerows(students)
        #for student in students:
        #    writer.writerow(student)
except Exception as e:
    print(e)