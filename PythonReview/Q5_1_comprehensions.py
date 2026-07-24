"""Use comprehensions and a generator for patient data."""


# Step 1: From a pile of patient cards, pull out different views: who has diabetes, each person’s latest vitals, every unique medicine, and a “high risk” list we can w...
def analyze_patients(patients: list[dict]) -> dict:
    # Step 2: list of patient ids that have diabetes
    diabetic = [p["id"] for p in patients if "diabetes" in p.get("conditions", [])]

    # Step 3: dictionary of each patient's latest vital reading
    latest = {p["id"]: p["vitals"][-1] for p in patients if p.get("vitals")}

    # Step 4: set of all unique medications across patients
    medications = {m for p in patients for m in p.get("medications", [])}

    # Step 5: generator that yields high-risk patient ids
    def high_risk():
        return (p["id"] for p in patients if p.get("risk_score", 0) >= 8)

    # Step 6: return list, dictionary, set, and generator together
    return {
        "diabetic_patients": diabetic,
        "latest_vitals": latest,
        "unique_medications": medications,
        "high_risk_generator": high_risk(),
    }


if __name__ == "__main__":
    r = analyze_patients(
        [
            {
                "id": "P1",
                "conditions": ["diabetes"],
                "vitals": [{"bp": 130}],
                "medications": ["aspirin"],
                "risk_score": 9,
            }
        ]
    )
    print(r["diabetic_patients"], list(r["high_risk_generator"]))
