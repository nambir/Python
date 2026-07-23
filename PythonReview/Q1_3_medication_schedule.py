"""Group and manage a patient's medication schedule."""
from collections import defaultdict
class MedicationSchedule:
    def __init__(self, medications: list[tuple[str, str]] = []):
        self.by_time: dict[str, list[str]] = defaultdict(list)
        for medication, time in medications: self.add(medication, time)
    def add(self, medication: str, time: str) -> None: self.by_time[time].append(medication)
    def remove(self, medication: str, time: str) -> bool:
        if medication not in self.by_time.get(time, []): return False
        self.by_time[time].remove(medication)
        if not self.by_time[time]: del self.by_time[time]
        return True
    def at(self, time: str) -> list[str]: return list(self.by_time.get(time, []))
    def grouped(self) -> dict[str, list[str]]: return {t: list(m) for t, m in self.by_time.items()}
def manage_medication_schedule(patient_medications: list[tuple[str, str]]) -> dict[str, list[str]]: return MedicationSchedule(patient_medications).grouped()
if __name__ == "__main__": print(manage_medication_schedule([("Aspirin","8:00"),("Insulin","8:00"),("Aspirin","20:00")]))
