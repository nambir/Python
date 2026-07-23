"""Traverse family history and interaction graphs recursively."""
def calculate_family_risk_score(family_tree:dict,condition:str,current_person:str,generation:int=0,visited=None)->float:
    visited=set() if visited is None else visited
    if current_person in visited or current_person not in family_tree:return 0.0
    visited.add(current_person); person=family_tree[current_person]
    own=1.0/(2**generation) if condition in person.get("conditions",[]) else 0.0
    return own+sum(calculate_family_risk_score(family_tree,condition,p,generation+1,visited) for p in person.get("parents",[]))
def find_medication_interactions(drug:str,interaction_tree:dict[str,set[str]],visited=None)->set[str]:
    visited=set() if visited is None else visited
    if drug in visited:return set()
    visited.add(drug); direct=set(interaction_tree.get(drug,set()))
    return direct|set().union(*(find_medication_interactions(d,interaction_tree,visited) for d in direct)) if direct else set()
if __name__ == "__main__": print(find_medication_interactions("a",{"a":{"b"},"b":{"c"}}))
