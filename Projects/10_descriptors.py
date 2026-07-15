"""Slide 10 — Descriptors / @property practice."""


class Celsius:
    def __init__(self):
        self._temp = 0.0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value: float):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._temp = value


if __name__ == "__main__":
    c = Celsius()
    c.temp = 25
    print("temp:", c.temp)
    try:
        c.temp = -300
    except ValueError as e:
        print("validation:", e)
