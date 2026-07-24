"""Evaluate educational patient eligibility facts."""


# Step 1: We answer four yes/no questions: scary symptoms? accepted insurance? bad history conflict? was history given at all? We do that by checking overlaps with kno...
def check_patient_eligibility(
    patient_age: int,
    symptoms: list[str],
    insurance_types: list[str],
    medical_history: list[str] | None,
) -> dict:
    # Step 2: define reference sets
    critical = {"chest_pain", "difficulty_breathing", "severe_bleeding"}
    accepted = {"medicare", "aetna", "bcbs", "cigna"}
    conflicting = {"organ_transplant", "active_bleeding"}

    # Step 3: convert symptoms/history to sets (missing history → empty for compare)
    symptom_set = set(symptoms)
    history = set(medical_history or [])

    # Step 4: detect overlap with critical symptoms
    has_critical_symptoms = bool(symptom_set & critical)

    # Step 5: detect overlap with accepted insurance
    insurance_accepted = bool(set(insurance_types) & accepted)

    # Step 6: detect overlap with conflicting history
    conflicting_history = bool(history & conflicting)

    # Step 7: record whether history was provided (None vs a list)
    history_provided = medical_history is not None

    # Step 8: return the four boolean results
    return {
        "has_critical_symptoms": has_critical_symptoms,
        "insurance_accepted": insurance_accepted,
        "conflicting_history": conflicting_history,
        "history_provided": history_provided,
    }


if __name__ == "__main__":
    print(check_patient_eligibility(50, ["chest_pain"], ["aetna"], None))
