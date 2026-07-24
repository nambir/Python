"""Schedule flexible appointments and update records."""


# Step 1: Booking a visit needs patient and doctor for sure; extra details and options are optional bags we pack along. Updating a record also has strict rules about w...
def schedule_appointment(patient_id, doctor_id, *appointment_details, **scheduling_options):
    # Step 2: require patient id and doctor id
    # Step 3: collect extra positional appointment details
    # Step 4: collect keyword scheduling options
    return {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "details": appointment_details,
        "options": scheduling_options,
    }


def update_patient_record(
    patient_id,
    /,
    name=None,
    age=None,
    *,
    blood_type=None,
    emergency_contact=None,
):
    # Step 5: patient_id positional-only; name/age optional; blood_type / contact keyword-only
    # Step 6: return structured dictionaries for both operations
    return {
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "blood_type": blood_type,
        "emergency_contact": emergency_contact,
    }


if __name__ == "__main__":
    print(schedule_appointment("P1", "D1", "2025-02-15", "10:00", priority="urgent"))
