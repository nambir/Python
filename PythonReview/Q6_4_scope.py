"""Demonstrate intentional global and local scope."""

# Step 2: shared hospital settings in a module-level configuration
HOSPITAL_CONFIG = {
    "max_patients_per_doctor": 50,
    "emergency_threshold_temp": 104.0,
    "default_appointment_duration": 30,
}


# Step 1: The hospital has shared settings on a notice board (global). Nested helpers can read that board, and one helper is allowed to update a number on it after che...
def patient_management_system():
    # Step 3: helper that reads capacity from the shared configuration
    def assign_doctor(patient_severity: str) -> dict:
        # Step 4: choose doctor type from severity; read shared capacity
        return {
            "severity": patient_severity,
            "capacity": HOSPITAL_CONFIG["max_patients_per_doctor"],
            "doctor_type": "emergency" if patient_severity == "critical" else "general",
        }

    def update_hospital_capacity(new_limit: int) -> None:
        # Step 5: validate then update the shared capacity
        if new_limit < 1:
            raise ValueError("limit must be positive")
        HOSPITAL_CONFIG["max_patients_per_doctor"] = new_limit

    # Step 6: return both helpers for callers
    return assign_doctor, update_hospital_capacity


if __name__ == "__main__":
    assign, update = patient_management_system()
    update(40)
    print(assign("critical"))
