"""Summarize immutable vital-sign readings."""


# Step 1: We have several days of blood pressure, temperature, and dates. We want simple summaries: average pressures, the hottest temperature, and the first-to-last d...
def process_vital_signs(
    readings: list[tuple[int, int, float, str]],
) -> tuple[float, float, float, tuple[str, str]]:
    # Step 2: require at least one reading
    if not readings:
        raise ValueError("at least one reading is required")

    # Step 3: separate into systolic, diastolic, temperature, date columns
    systolic, diastolic, temperatures, dates = zip(*readings)

    # Step 4: average systolic and diastolic
    avg_sys = sum(systolic) / len(systolic)
    avg_dia = sum(diastolic) / len(diastolic)

    # Step 5: highest temperature
    max_temp = max(temperatures)

    # Step 6: earliest and latest dates
    date_range = (min(dates), max(dates))

    # Step 7: return averages, max temperature, and date range
    return (avg_sys, avg_dia, max_temp, date_range)


if __name__ == "__main__":
    print(process_vital_signs([(120, 80, 98.6, "2024-01-15"), (115, 75, 99.1, "2024-01-16")]))
