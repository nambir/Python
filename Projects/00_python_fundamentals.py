"""Slide 1 — What is Python? Interpretation, indentation, dynamic typing."""

# INTERPRETATION: python this_file.py
#   .py source -> bytecode (.pyc) -> CPython interpreter executes it

if __name__ == "__main__":
    print("=== Interpretation ===")
    print("Running:", __file__)
    print("CPython compiles to bytecode, then interprets it.")

    print("\n=== Indentation (blocks) ===")
    score = 75
    if score >= 60:
        print("Pass - indentation defines this block")
    else:
        print("Fail")

    print("\n=== Dynamic typing ===")
    x = 42
    print("x as int:", x, type(x))
    x = "hello"
    print("x as str:", x, type(x))

    print("\n=== Duck typing ===")

    class Dog:
        def speak(self):
            return "Woof!"

    def announce(animal):
        return animal.speak()

    print(announce(Dog()))
