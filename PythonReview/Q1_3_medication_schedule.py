"""Group and manage a patient's medication schedule."""
from collections import defaultdict


# Step 1: Medicines must be taken at different times. We put each medicine into a "box" labeled with its time, so we can quickly see what to take at 8:00 or add/remove one later.
class MedicationSchedule:
    def __init__(self, medications: list[tuple[str, str]] = []):
        # Step 2–3: maintain schedule as a dictionary; start empty (time -> medicines)
        self.by_time: dict[str, list[str]] = defaultdict(list)
        # Steps 4–7: read each (medicine, time); ensure key exists; append medicine
        for medication, time in medications:
            self.add(medication, time)

    def add(self, medication: str, time: str) -> None:
        # Step 8: add medication — create time list if missing, then append
        self.by_time[time].append(medication)

    def remove(self, medication: str, time: str) -> bool:
        # Step 9: remove medication if present; delete empty time keys
        if medication not in self.by_time.get(time, []):
            return False
        self.by_time[time].remove(medication)
        if not self.by_time[time]:
            del self.by_time[time]
        return True

    def at(self, time: str) -> list[str]:
        # Step 10: get medications for a time, or empty list if missing
        return list(self.by_time.get(time, []))

    def grouped(self) -> dict[str, list[str]]:
        # Step 11: return the final medication schedule
        return {t: list(m) for t, m in self.by_time.items()}


def manage_medication_schedule(patient_medications: list[tuple[str, str]]) -> dict[str, list[str]]:
    # Steps 2–11 via the class, then return the final schedule
    return MedicationSchedule(patient_medications).grouped()


if __name__ == "__main__":
    print(manage_medication_schedule([("Aspirin", "8:00"), ("Insulin", "8:00"), ("Aspirin", "20:00")]))
