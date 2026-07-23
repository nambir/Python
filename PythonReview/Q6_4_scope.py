"""Demonstrate intentional global and local scope."""
HOSPITAL_CONFIG={"max_patients_per_doctor":50,"emergency_threshold_temp":104.0,"default_appointment_duration":30}
def patient_management_system():
    def assign_doctor(patient_severity:str)->dict: return {"severity":patient_severity,"capacity":HOSPITAL_CONFIG["max_patients_per_doctor"],"doctor_type":"emergency" if patient_severity=="critical" else "general"}
    def update_hospital_capacity(new_limit:int)->None:
        if new_limit<1: raise ValueError("limit must be positive")
        HOSPITAL_CONFIG["max_patients_per_doctor"]=new_limit
    return assign_doctor,update_hospital_capacity
if __name__ == "__main__": assign,update=patient_management_system(); update(40); print(assign("critical"))
