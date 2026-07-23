"""Process patient vitals with assignment expressions."""
def process_patient_vitals(patients_data:list[dict])->list[dict]:
    results=[]
    for patient in patients_data:
        flags=[]
        if (bmi:=patient["weight_kg"]/patient["height_m"]**2)>30: flags.append(f"obesity BMI={bmi:.1f}")
        if (temp:=patient.get("temperature",0))>=100.4: flags.append(f"fever {temp}")
        if (count:=len(patient.get("medications",[])))>5: flags.append(f"polypharmacy {count}")
        if flags: results.append({"id":patient["id"],"flags":flags})
    return results
if __name__ == "__main__": print(process_patient_vitals([{"id":"P1","weight_kg":95,"height_m":1.7,"temperature":101,"medications":["a"]*6}]))
