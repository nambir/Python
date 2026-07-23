"""Use comprehensions and a generator for patient data."""
def analyze_patients(patients:list[dict])->dict:
    diabetic=[p["id"] for p in patients if "diabetes" in p.get("conditions",[])]
    latest={p["id"]:p["vitals"][-1] for p in patients if p.get("vitals")}
    medications={m for p in patients for m in p.get("medications",[])}
    def high_risk(): return (p["id"] for p in patients if p.get("risk_score",0)>=8)
    return {"diabetic_patients":diabetic,"latest_vitals":latest,"unique_medications":medications,"high_risk_generator":high_risk()}
if __name__ == "__main__": r=analyze_patients([{"id":"P1","conditions":["diabetes"],"vitals":[{"bp":130}],"medications":["aspirin"],"risk_score":9}]); print(r["diabetic_patients"],list(r["high_risk_generator"]))
