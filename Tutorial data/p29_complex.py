class Complex:

    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im

    def __repr__(self):
        return f"Complex(re={self.re}, im={self.im})"

    def __str__(self):
        if self.im > 0:
            return f"{self.re} + {self.im}i"
        return f"{self.re} {self.im}i"

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __len__(self):  # musí vracet int
        return int((self.re ** 2 + self.im ** 2) ** (1/2))

    def len(self):
        return (self.re ** 2 + self.im ** 2) ** (1/2)


c1 = Complex(1, 1)
print(f"c1 = {c1}")
c2 = Complex(-2, -3)
print(f"c2 = {c2}")
print(f"c1 + c2 = {c1 + c2}")
print(f"c1 - c2 = {c1 - c2}")
c3 = Complex(1, 1)
print(f"c1 == c3: {c1 == c3}")
print(f"len(c1) = {len(c1)}")  # c1.__len__
print(f"c1.len() = {c1.len()}")

for i in range(len(c1)):
    pass
