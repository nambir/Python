"""Calculate an educational hospital-stay bill."""
from decimal import Decimal, ROUND_HALF_UP


# Step 1: A hospital stay costs money each day. We multiply days by the daily room price, take off an insurance discount if they have it, and show the final bill.
def calculate_patient_bill(
    room_charge_per_day: float,
    days_stayed: int,
    has_insurance: bool,
    patient_name: str,
) -> dict:
    # Step 2: validate that money and day inputs are usable
    if room_charge_per_day < 0 or days_stayed < 0:
        raise ValueError("charges and days must be non-negative")

    # Step 3: calculate stay subtotal (daily charge × days)
    subtotal = Decimal(str(room_charge_per_day)) * days_stayed

    # Step 4: apply 20% insurance discount, or zero if no insurance
    discount = subtotal * Decimal("0.20") if has_insurance else Decimal("0")

    # Step 5: subtract discount and round money to 2 decimal places
    final = (subtotal - discount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # Step 6: return patient details with money breakdown
    return {
        "patient_name": patient_name,
        "days_stayed": days_stayed,
        "subtotal": subtotal,
        "discount": discount,
        "final_amount": final,
    }


if __name__ == "__main__":
    print(calculate_patient_bill(350.0, 3, True, "Asha"))
