a = "Global"

def outer():
    a = "Enclosing"

    def inner():
        a = "Local"
        print(f"a - inner: {a}")

    inner()
    print(f"a - outer: {a}")

outer()
print(f"a - global: {a}")