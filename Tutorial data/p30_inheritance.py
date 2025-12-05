class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname})"

    def __str__(self):
        return f"{self._name} {self.surname}"

    def full_name(self):
        return f"{self.surname} {self._name}"

    def set_name(self, name: str):
        self.name = name.strip().capitalize()

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, name: str):
        self._name = name.strip().capitalize()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        self._surname = surname.strip().capitalize()


class Student(Person):
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname)  # nejprve vytvoříme člověka (Person)
        self.age = age
        self.grades = []

    def __repr__(self):
        return f"Student(name={self.name}, surname={self.surname}, age={self.age})"

    def __str__(self):
        return f"{self.name} {self.surname} ({self.age} let)"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Věk nesmí být záporný.")

    def add_grade(self, grade: int):
        #if grade >= 1 and grade <= 5:
        if 1 <= grade <= 5:
            self.grades.append(grade)
        else:
            raise ValueError

    def average_grade(self):
        if len(self.grades):
            return sum(self.grades) / len(self.grades)
        return None


person1 = Person("   adam   ", "   bernau    ")
person1.name = "  aleš     "
print(f"{person1.name}")
#person1._name = "Adalbert"  # stále mám přímý přístup
#person1.set_name("   aleš   ")
person1.surname = "    bodocký   "
print(f"person1 = {person1}")

student1 = Student("Božetěcha", "Nováková", 10)
print(f"student1 = {student1}")
print(f"[student1] = {[student1]}")
print(f"student1.full_name() = {student1.full_name()}")
print(f"person1.full_name() = {person1.full_name()}")

print(f"student1.average_grade() = {student1.average_grade()}")
student1.grades.append(1)  # můžu přidávat hodnocení přímo (mám přímý přístup k atributu)
student1.add_grade(2)      # nebo můžu použít metodu
print(f"student1.grades = {student1.grades}")
print(f"student1.average_grade() = {student1.average_grade()}")

student2 = Student("Cecílie", "Svobodová", 22)
student2.add_grade(2)
student2.add_grade(3)
student2.add_grade(2)

students = [student1, student2]
for student in students:
    print(f"Student {student} má známky {student.grades}, průměr známek je: {student.average_grade()}")


class Class:
    def __init__(self, name: str, teacher: Person):
        self.name = name
        self.teacher = teacher
        self.students = []

    def __repr__(self):
        return f"Class(name={self.name}, teacher={self.teacher})"


class1 = Class("4.B", Person("Jan", "Učitel"))
print(f"class1 = {class1}")
class1.students.extend([
    Student("Alžběta", "Nová", 15),
    Student("Bára", "Durovková", 14),
    Student("Cecílie", "Svobodová", 15),
    Student("Dušan", "Novák", 14),
    Student("Evžen", "Brzobohatý", 15),
    Student("    filip   ", "   rychlechudý   ", 14)
])
for student in class1.students:
    print(f"Student {student} má známky {student.grades} a jeho průměr je {student.average_grade()}")
