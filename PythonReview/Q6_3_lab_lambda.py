"""Process laboratory results with lambda functions."""
def process_lab_results(lab_data:list[dict])->dict:
    deviation=lambda r:max(r["normal_range"][0]-r["value"],r["value"]-r["normal_range"][1],0)
    abnormal=list(filter(lambda r:deviation(r)>0,lab_data)); scores=list(map(lambda r:{"test":r["test"],"severity":deviation(r)},lab_data))
    return {"abnormal":abnormal,"severity_scores":scores,"priority_order":sorted(lab_data,key=deviation,reverse=True)}
if __name__ == "__main__": print(process_lab_results([{"test":"glucose","value":120,"normal_range":(70,100)}]))
