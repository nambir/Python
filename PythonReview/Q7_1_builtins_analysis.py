"""Analyze simple medical records with Python built-ins."""
from functools import reduce
def medical_data_analysis(patient_records:list[dict],lab_results:list[tuple[str,list[float]]])->dict:
    ages=list(map(lambda p:p["age"],patient_records)); elderly=list(filter(lambda p:p["age"]>65,patient_records))
    most=reduce(lambda a,b:a if len(a["medications"])>=len(b["medications"]) else b,patient_records) if patient_records else None
    return {"ages":ages,"elderly_patients":elderly,"combined_data":list(zip(patient_records,lab_results)),"indexed_patients":list(enumerate(patient_records)),"patient_most_meds":most,"risk_sorted":sorted(patient_records,key=lambda p:(p["age"],len(p["medications"])),reverse=True),"statistics":{"min_age":min(ages,default=None),"max_temp":max((v[2] for _,v in lab_results),default=None)},"data_types":{pid:type(data).__name__ for pid,data in lab_results},"available_slots":list(range(8,17))}
if __name__ == "__main__": print(medical_data_analysis([{"id":"P1","age":67,"medications":["a","b"]}],[("P1",[120,80,98.6])]))
