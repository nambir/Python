"""Apply educational vital-sign triage rules."""


# Step 1: Like a traffic light for sick patients: check the scariest warning signs first (Critical), then medium ones (Urgent), otherwise they are Standard.
def triage_patient(
    temperature: float,
    blood_pressure: tuple[int, int],
    heart_rate: int,
    is_conscious: bool,
    pain_level: int,
) -> str:
    # Step 2: read systolic and diastolic from the BP pair
    sys, dia = blood_pressure

    # Step 3: if any critical rule matches, return Critical
    if temperature > 104 or sys > 180 or dia > 120 or heart_rate > 120 or not is_conscious:
        return "Critical"

    # Step 4: else if any urgent rule matches, return Urgent
    if temperature > 101 or sys > 140 or dia > 90 or pain_level > 7:
        return "Urgent"

    # Step 5: otherwise return Standard
    return "Standard"


if __name__ == "__main__":
    print(triage_patient(102, (130, 85), 90, True, 4))
