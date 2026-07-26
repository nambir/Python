def process_vital_signs(readings: list) -> tuple:
    """
    Process vital signs readings and return statistics
    Input: [(120, 80, 98.6, '2024-01-15'), (115, 75, 99.1, '2024-01-16')]
    Output: Tuple of (avg_systolic, avg_diastolic, max_temp, date_range)
    """
    systolic_list = []
    diastolic_list = []
    temp_list = []
    date_list = []
    systolic_list, diastolic_list, temp_list, date_list = zip(*readings)
    avg_systolic = sum(systolic_list) / len(systolic_list)
    avg_diastolic = sum(diastolic_list) / len(diastolic_list)
    max_temp = max(temp_list)
    date_range = (min(date_list), max(date_list))
    return avg_systolic, avg_diastolic, max_temp, date_range

result = process_vital_signs([(120, 80, 98.6, '2024-01-15'), (115, 75, 99.1, '2024-01-16')])
print(result)
