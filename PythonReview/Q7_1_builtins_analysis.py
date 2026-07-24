"""Analyze simple medical records with Python built-ins."""
from functools import reduce


# Step 1: We use Python’s built-in tools like a toolbox: pull ages, filter older patients, pair records with labs, sort by risk, and compute simple min/max stats.
def medical_data_analysis(
    patient_records: list[dict],
    lab_results: list[tuple[str, list[float]]],
) -> dict:
    # Step 2: extract ages with map; filter elderly patients
    ages = list(map(lambda p: p["age"], patient_records))
    elderly = list(filter(lambda p: p["age"] > 65, patient_records))

    # Step 3: reduce to the patient with the most medications
    most = (
        reduce(
            lambda a, b: a if len(a["medications"]) >= len(b["medications"]) else b,
            patient_records,
        )
        if patient_records
        else None
    )

    # Step 4: pair records with labs (zip); number patients (enumerate)
    combined = list(zip(patient_records, lab_results))
    indexed = list(enumerate(patient_records))

    # Step 5: sort patients by risk-related keys
    risk_sorted = sorted(
        patient_records,
        key=lambda p: (p["age"], len(p["medications"])),
        reverse=True,
    )

    # Step 6: simple statistics with min and max
    min_age = min(ages, default=None)
    max_temp = max((v[2] for _, v in lab_results), default=None)

    # Step 7: record types with type(); time slots with range()
    data_types = {pid: type(data).__name__ for pid, data in lab_results}
    available_slots = list(range(8, 17))

    # Step 8: return all analysis pieces in one dictionary
    return {
        "ages": ages,
        "elderly_patients": elderly,
        "combined_data": combined,
        "indexed_patients": indexed,
        "patient_most_meds": most,
        "risk_sorted": risk_sorted,
        "statistics": {"min_age": min_age, "max_temp": max_temp},
        "data_types": data_types,
        "available_slots": available_slots,
    }


if __name__ == "__main__":
    print(
        medical_data_analysis(
            [{"id": "P1", "age": 67, "medications": ["a", "b"]}],
            [("P1", [120, 80, 98.6])],
        )
    )
