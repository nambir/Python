"""Process laboratory results with lambda functions."""


# Step 1: Each lab test has a “normal” window. We measure how far outside that window a value is, list the bad ones, score them, and sort the worst first.
def process_lab_results(lab_data: list[dict]) -> dict:
    # Step 2: define how far a value sits outside its normal range (0 if inside)
    deviation = lambda r: max(r["normal_range"][0] - r["value"], r["value"] - r["normal_range"][1], 0)

    # Step 3: filter rows that are outside range
    abnormal = list(filter(lambda r: deviation(r) > 0, lab_data))

    # Step 4: map each row to a severity score
    scores = list(map(lambda r: {"test": r["test"], "severity": deviation(r)}, lab_data))

    # Step 5: sort all rows by severity (worst first)
    priority_order = sorted(lab_data, key=deviation, reverse=True)

    # Step 6: return abnormal rows, scores, and priority order
    return {
        "abnormal": abnormal,
        "severity_scores": scores,
        "priority_order": priority_order,
    }


if __name__ == "__main__":
    print(process_lab_results([{"test": "glucose", "value": 120, "normal_range": (70, 100)}]))
