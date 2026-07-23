"""Calculate an educational hospital-stay bill."""
from decimal import Decimal, ROUND_HALF_UP
def calculate_patient_bill(room_charge_per_day: float, days_stayed: int, has_insurance: bool, patient_name: str) -> dict:
    if room_charge_per_day < 0 or days_stayed < 0: raise ValueError("charges and days must be non-negative")
    subtotal = Decimal(str(room_charge_per_day)) * days_stayed
    discount = subtotal * Decimal("0.20") if has_insurance else Decimal("0")
    final = (subtotal - discount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {"patient_name": patient_name, "days_stayed": days_stayed, "subtotal": subtotal, "discount": discount, "final_amount": final}
if __name__ == "__main__": print(calculate_patient_bill(350.0, 3, True, "Asha"))
