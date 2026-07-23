"""Validate typed patient data."""
from dataclasses import dataclass
from enum import Enum
class BloodType(Enum): A_POS="A+"; A_NEG="A-"; B_POS="B+"; B_NEG="B-"; AB_POS="AB+"; AB_NEG="AB-"; O_POS="O+"; O_NEG="O-"
@dataclass(frozen=True)
class VitalSigns: systolic:int; diastolic:int; temperature:float; heart_rate:int; timestamp:str
def validate_patient_data(patient_id: str, age: int, blood_type: BloodType, vitals: list[VitalSigns], emergency_contact: dict[str,str] | None=None) -> bool:
    if not patient_id.strip() or not 0 <= age <= 130 or not isinstance(blood_type, BloodType) or not vitals: return False
    if emergency_contact is not None and not {"name","phone"} <= emergency_contact.keys(): return False
    return all(40 <= v.systolic <= 260 and 20 <= v.diastolic <= 180 and 85 <= v.temperature <= 110 and 20 <= v.heart_rate <= 250 for v in vitals)
if __name__ == "__main__": print(validate_patient_data("P1",42,BloodType.O_POS,[VitalSigns(120,80,98.6,72,"2025-01-01")]))
