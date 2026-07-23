"""Apply educational vital-sign triage rules."""
def triage_patient(temperature:float,blood_pressure:tuple[int,int],heart_rate:int,is_conscious:bool,pain_level:int)->str:
    sys,dia=blood_pressure
    if temperature>104 or sys>180 or dia>120 or heart_rate>120 or not is_conscious: return "Critical"
    if temperature>101 or sys>140 or dia>90 or pain_level>7: return "Urgent"
    return "Standard"
if __name__ == "__main__": print(triage_patient(102,(130,85),90,True,4))
