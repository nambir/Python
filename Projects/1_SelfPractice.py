def calculate_patient_bill(room_charge_per_day: float, days_stayed: int, 
                          has_insurance: bool, patient_name: str) -> dict:
    Amount= room_charge_per_day* days_stayed;
    if has_insurance:
        Amount= Amount*0.80;
    return { "patient_name" : patient_name ,"Amount": Amount }

print(calculate_patient_bill(100, 5, True, "John"))
print(calculate_patient_bill(100, 5, False, "John"))
