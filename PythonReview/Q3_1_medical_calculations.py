"""Calculate educational BMI and dosage values."""
import math


# Step 1: We calculate BMI from weight and height, maybe lower the medicine dose for older patients, figure out how many days a bottle lasts, and say if BMI looks heal...
def medical_calculations(
    weight_kg: float,
    height_m: float,
    base_dosage_mg: float,
    patient_age: int,
) -> dict:
    # Step 2: reject non-positive height or dosage
    if height_m <= 0 or base_dosage_mg <= 0:
        raise ValueError("height and dosage must be positive")

    # Step 3: calculate BMI from weight and height
    bmi = weight_kg / height_m**2

    # Step 4: reduce dosage for age over 65; otherwise keep base
    dosage = base_dosage_mg * (0.9 if patient_age > 65 else 1)

    # Step 5: estimate days of supply from fixed total ÷ dosage
    days_supply = math.floor(1000 / dosage)

    # Step 6: flag whether BMI is in the healthy range
    healthy_bmi = 18.5 <= bmi <= 24.9

    # Step 7: return BMI, dosage, days supply, and healthy flag
    return {
        "bmi": round(bmi, 2),
        "adjusted_dosage_mg": round(dosage, 2),
        "days_supply": days_supply,
        "healthy_bmi": healthy_bmi,
    }


if __name__ == "__main__":
    print(medical_calculations(70, 1.75, 50, 70))
