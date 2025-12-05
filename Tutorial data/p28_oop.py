class Car:
    spz = ""


my_car = Car()
my_car.spz = "AB123456"
print(my_car)
print(my_car.spz)

my_car.color = "red"
print(my_car.color)

my_car2 = Car()
#print(my_car2.color)  # AttributeError: 'Car' object has no attribute 'color'


class Person:
    """gender = ""
    _name = ""
    _surname = ""
    _age = 0"""

    # konstruktor - volá se při vytváření objektu
    def __init__(self, name: str, surname: str, age: int):
        print("Vytvářím objekt třídy Person")
        self._name = name
        self._surname = surname
        self._age = age
        self.gender = ""
        #self.height = None
        #self.gender = None
        #self.parent = Person

    def __repr__(self):
        return f"Person(name={self._name}, surname={self._surname}, age={self._age})"

    """def to_string(self):
        return f"Person(name={self._name}, surname={self._surname}, age={self._age})"""""

    def __str__(self):
        return f"{self._name} {self._surname} ({self._age} let)"

    def full_name(self):
        return f"{self._name} {self._surname}"


adam = Person()#"Adam", "Bernau", 12)
adam._name = "Adam"
adam._surname = "Beranu"
adam._age = 12
print(f"{adam._name} {adam._surname} ({adam._age} let)")
print(adam)
print(adam.__repr__())
"""
print("="*80)
bedrich = Person()#"Bedřich", "Smetana", 70)
persons = [adam, bedrich]
print(persons[0])  # použije se __str__
print(persons)     # použije se __repr__
print(adam.full_name())
"""