"""Calculate educational BMI and dosage values."""
import math
def medical_calculations(weight_kg: float,height_m: float,base_dosage_mg: float,patient_age: int)->dict:
    if height_m <= 0 or base_dosage_mg <= 0: raise ValueError("height and dosage must be positive")
    bmi=weight_kg/height_m**2; dosage=base_dosage_mg*(.9 if patient_age>65 else 1)
    return {"bmi":round(bmi,2),"adjusted_dosage_mg":round(dosage,2),"days_supply":math.floor(1000/dosage),"healthy_bmi":18.5<=bmi<=24.9}
if __name__ == "__main__": print(medical_calculations(70,1.75,50,70))
