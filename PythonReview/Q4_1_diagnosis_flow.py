"""Run an educational, non-clinical assessment workflow."""


# Step 1: Decide what to do in order of urgency: emergencies first, then long-term issues, then common colds, else “need more tests.” Extra helpers make check-in messa...
def diagnose_patient(
    symptoms: list[str],
    vital_signs: dict,
    medical_history: list[str],
    lab_results: dict,
) -> dict:
    # Step 2: check emergency conditions first
    if {"chest_pain", "severe_bleeding"} & set(symptoms) or vital_signs.get("temperature", 0) > 104:
        return {"priority": "emergency", "action": "immediate evaluation"}

    # Step 3: else check chronic indicators
    if "diabetes" in medical_history and lab_results.get("glucose", 0) > 180:
        return {"priority": "chronic", "action": "review glucose management"}

    # Step 4: else check common-ailment indicators
    if "cough" in symptoms and vital_signs.get("temperature", 0) > 100.4:
        return {"priority": "common", "action": "clinical assessment"}

    # Step 5: default — further testing
    return {"priority": "unknown", "action": "further testing required"}


def patient_monitoring_loop(patient_id: str, monitoring_duration_hours: int) -> list[str]:
    # Step 6: emit a status message every 30 minutes
    return [
        f"{patient_id}: checked at {minute} minutes"
        for minute in range(0, monitoring_duration_hours * 60, 30)
    ]


def daily_medication_schedule(patient_medications: dict[str, list[str]]) -> list[str]:
    # Step 7: flatten each time → drug list into take instructions
    return [f"{time}: take {drug}" for time, drugs in patient_medications.items() for drug in drugs]


if __name__ == "__main__":
    print(diagnose_patient(["cough"], {"temperature": 101}, [], {}))
