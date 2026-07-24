"""Check educational drug-interaction pairs."""


# Step 1: Before giving a new medicine, check if it fights with medicines the patient already takes. We look up known bad pairs and see if any of those partners are al...
def check_drug_interactions(
    current_medications: set[str],
    new_medication: str,
    interaction_db: dict[str, set[str]],
) -> dict:
    # Step 2: normalize names for case-insensitive comparison
    current = {m.lower() for m in current_medications}
    new = new_medication.lower()

    # Step 3: look up interaction partners for the new medication
    partners = {m.lower() for m in interaction_db.get(new, set())}

    # Step 4: find overlap between current meds and partners
    conflicts = current & partners

    # Step 5: safe only when there is no overlap
    safe = not conflicts

    # Step 6: return safety, conflicts, and a short recommendation
    return {
        "safe": safe,
        "interactions": conflicts,
        "recommendations": (
            ["Consult a clinician before prescribing."]
            if conflicts
            else ["No listed interaction; still verify clinically."]
        ),
    }


if __name__ == "__main__":
    print(check_drug_interactions({"warfarin"}, "aspirin", {"aspirin": {"warfarin"}}))
