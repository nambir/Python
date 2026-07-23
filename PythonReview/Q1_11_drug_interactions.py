"""Check educational drug-interaction pairs."""
def check_drug_interactions(current_medications: set[str], new_medication: str, interaction_db: dict[str, set[str]]) -> dict:
    current = {m.lower() for m in current_medications}; new = new_medication.lower()
    conflicts = current & {m.lower() for m in interaction_db.get(new, set())}
    return {"safe": not conflicts, "interactions": conflicts, "recommendations": ["Consult a clinician before prescribing."] if conflicts else ["No listed interaction; still verify clinically."]}
if __name__ == "__main__": print(check_drug_interactions({"warfarin"}, "aspirin", {"aspirin":{"warfarin"}}))
