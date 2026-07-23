"""Manage nested patient records in memory."""
class PatientRecords:
    def __init__(self): self.records: dict[str, dict] = {}
    def add(self, patient_id: str, personal: dict, medical: dict) -> None:
        if patient_id in self.records: raise ValueError("patient already exists")
        self.records[patient_id] = {"personal": dict(personal), "medical": dict(medical), "visits": []}
    def update(self, patient_id: str, **changes) -> None: self.records[patient_id].update(changes)
    def by_blood_type(self, blood_type: str) -> list[str]: return [pid for pid,r in self.records.items() if r["medical"].get("blood_type","").upper() == blood_type.upper()]
    def visits(self, patient_id: str) -> list[dict]: return list(self.records[patient_id]["visits"])
if __name__ == "__main__": 
    db=PatientRecords(); db.add("P1",{"name":"John","age":45},{"blood_type":"O+","allergies":["penicillin"]}); print(db.by_blood_type("o+"))
