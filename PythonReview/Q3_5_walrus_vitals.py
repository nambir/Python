"""Process patient vitals with assignment expressions."""


# Step 1: Walk through each patient once. While looking, note problems (high BMI, fever, too many medicines). Keep only the patients who got at least one note.
def process_patient_vitals(patients_data: list[dict]) -> list[dict]:
    # Step 2: prepare an empty results list
    results = []

    for patient in patients_data:
        # Step 3: start an empty flags list for this patient
        flags = []

        # Step 4: compute BMI; flag obesity when BMI > 30
        if (bmi := patient["weight_kg"] / patient["height_m"] ** 2) > 30:
            flags.append(f"obesity BMI={bmi:.1f}")

        # Step 5: read temperature; flag fever when high enough
        if (temp := patient.get("temperature", 0)) >= 100.4:
            flags.append(f"fever {temp}")

        # Step 6: count medications; flag polypharmacy when count is large
        if (count := len(patient.get("medications", []))) > 5:
            flags.append(f"polypharmacy {count}")

        # Step 7: keep patient id and flags when any flag exists
        if flags:
            results.append({"id": patient["id"], "flags": flags})

    # Step 8: return only the flagged patients
    return results


if __name__ == "__main__":
    print(
        process_patient_vitals(
            [{"id": "P1", "weight_kg": 95, "height_m": 1.7, "temperature": 101, "medications": ["a"] * 6}]
        )
    )
