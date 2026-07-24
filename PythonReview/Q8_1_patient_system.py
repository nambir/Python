"""A small integrated, educational patient-management system."""


# Step 1: Build a tiny hospital app: store patients, add them carefully, attach vitals, print a filtered report, and run a list of jobs on the whole system.
class PatientManagementSystem:
    def __init__(self):
        # Step 2: initialize an empty patient store
        self.patients: dict[str, dict] = {}

    def add_patient(self, **patient_data):
        # Step 3: add only when id is a non-empty string and not a duplicate
        patient_id = patient_data.get("id")
        if not isinstance(patient_id, str) or not patient_id:
            raise ValueError("a non-empty id is required")
        if patient_id in self.patients:
            raise ValueError("duplicate id")
        self.patients[patient_id] = {**patient_data, "vitals": []}

    def update_vitals(self, patient_id: str, *vitals, **metadata):
        # Step 4: append vitals (positional values + optional metadata)
        self.patients[patient_id]["vitals"].append({"values": tuple(vitals), **metadata})

    def generate_report(self, filter_func=lambda p: True):
        # Step 5: yield patients that pass an optional filter
        return ({"id": pid, **p} for pid, p in self.patients.items() if filter_func(p))

    def batch_process(self, operations: list):
        # Step 6: run each operation against the system and collect results
        return list(map(lambda operation: operation(self), operations))


if __name__ == "__main__":
    system = PatientManagementSystem()
    system.add_patient(id="P1", name="Asha", age=42)
    system.update_vitals("P1", 120, 80, 98.6, at="09:00")
    print(list(system.generate_report()))
