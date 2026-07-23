"""Summarize immutable vital-sign readings."""
def process_vital_signs(readings: list[tuple[int, int, float, str]]) -> tuple[float, float, float, tuple[str, str]]:
    if not readings: raise ValueError("at least one reading is required")
    systolic, diastolic, temperatures, dates = zip(*readings)
    return (sum(systolic)/len(systolic), sum(diastolic)/len(diastolic), max(temperatures), (min(dates), max(dates)))
if __name__ == "__main__": print(process_vital_signs([(120,80,98.6,"2024-01-15"),(115,75,99.1,"2024-01-16")]))
