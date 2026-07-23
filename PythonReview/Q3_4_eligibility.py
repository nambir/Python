"""Evaluate educational patient eligibility facts."""
def check_patient_eligibility(patient_age:int,symptoms:list[str],insurance_types:list[str],medical_history:list[str] | None)->dict:
    critical={"chest_pain","difficulty_breathing","severe_bleeding"}; accepted={"medicare","aetna","bcbs","cigna"}; conflicting={"organ_transplant","active_bleeding"}
    symptom_set=set(symptoms); history=set(medical_history or [])
    return {"has_critical_symptoms":bool(symptom_set&critical),"insurance_accepted":bool(set(insurance_types)&accepted),"conflicting_history":bool(history&conflicting),"history_provided":medical_history is not None}
if __name__ == "__main__": print(check_patient_eligibility(50,["chest_pain"],["aetna"],None))
