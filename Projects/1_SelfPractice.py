"""    Check for drug interactions before prescribing new medication    
    interaction_db = {
        'aspirin': {'warfarin', 'heparin'},
        'warfarin': {'aspirin', 'vitamin_k'},
        ...
    }    
    Return: {
        'safe': bool,
        'interactions': set of conflicting drugs,
        'recommendations': list
    }
    """
def check_drug_interactions(
    current_medications: set[str],
    new_medication: str,
    interaction_db: dict[str, set[str]],
) -> dict:

    # Step 2: look up interaction partners for the new medication
    conflictingMedicinesForNewMedicine = interaction_db.get(new_medication, set())
    # Step 3: find overlap between current meds and partners
    print(conflictingMedicinesForNewMedicine)
    print(current_medications)
    if conflictingMedicinesForNewMedicine.intersection(current_medications):
        conflictStatus = True
    else:
        conflictStatus = False
    return {
        "safe": False if conflictStatus else True ,
        "interactions": conflictingMedicinesForNewMedicine.intersection(current_medications) if conflictStatus else set(),
        "recommendations": ["Consult a clinician before prescribing."] if conflictStatus else ["No listed interaction; still verify clinically."]
    }

existingMedications = {"warfarin"}
newMedication = "aspirin"
interactionDB = {"aspirin": {"warfarin"}}

result = check_drug_interactions(existingMedications, newMedication, interactionDB)
print(result)
