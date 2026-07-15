"""Slide 8 — OOP Concepts practice."""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class BankAccount:
    def __init__(self, balance: float):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"BankAccount(balance={self._balance})"

    def __repr__(self):
        return f"BankAccount({self._balance!r})"


if __name__ == "__main__":
    for pet in [Dog("Rex"), Cat("Luna")]:
        print(pet.speak())
    acct = BankAccount(1000)
    print(acct)
    print(repr(acct))
    print("Dog MRO:", Dog.__mro__)
