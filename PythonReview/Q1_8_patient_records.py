"""Manage nested patient records in memory."""


# Step 1: Think of a filing cabinet: each patient gets one folder (by id) with personal info, medical info, and visits. We add folders, update them, and search by bloo...
class PatientRecords:
    def __init__(self):
        # Step 2: keep records in a dictionary keyed by patient id
        self.records: dict[str, dict] = {}

    def add(self, patient_id: str, personal: dict, medical: dict) -> None:
        # Step 3: reject duplicates; store personal, medical, empty visits
        if patient_id in self.records:
            raise ValueError("patient already exists")
        self.records[patient_id] = {
            "personal": dict(personal),
            "medical": dict(medical),
            "visits": [],
        }

    def update(self, patient_id: str, **changes) -> None:
        # Step 4: merge new fields into the existing record
        self.records[patient_id].update(changes)

    def by_blood_type(self, blood_type: str) -> list[str]:
        # Step 5: collect ids whose medical blood type matches
        return [
            pid
            for pid, r in self.records.items()
            if r["medical"].get("blood_type", "").upper() == blood_type.upper()
        ]

    def visits(self, patient_id: str) -> list[dict]:
        # Step 6: return a copy of that patient's visits
        return list(self.records[patient_id]["visits"])


if __name__ == "__main__":
    db = PatientRecords()
    db.add("P1", {"name": "John", "age": 45}, {"blood_type": "O+", "allergies": ["penicillin"]})
    print(db.by_blood_type("o+"))
