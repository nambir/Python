"""Traverse family history and interaction graphs recursively."""


# Step 1: Family risk is like climbing a family tree: if someone has the condition, add a score that gets smaller the farther up you go. Drug interactions are like fol...
def calculate_family_risk_score(
    family_tree: dict,
    condition: str,
    current_person: str,
    generation: int = 0,
    visited=None,
) -> float:
    # Step 2: track visited people so recursion does not loop
    visited = set() if visited is None else visited

    # Step 3: stop with zero when missing or already visited
    if current_person in visited or current_person not in family_tree:
        return 0.0
    visited.add(current_person)
    person = family_tree[current_person]

    # Step 4: score current person if they have the condition, scaled by generation
    own = 1.0 / (2**generation) if condition in person.get("conditions", []) else 0.0

    # Step 5: add scores from each parent one generation deeper
    # Step 7: return accumulated score
    return own + sum(
        calculate_family_risk_score(family_tree, condition, p, generation + 1, visited)
        for p in person.get("parents", [])
    )


def find_medication_interactions(
    drug: str,
    interaction_tree: dict[str, set[str]],
    visited=None,
) -> set[str]:
    # Step 2: track visited drugs so recursion does not loop
    visited = set() if visited is None else visited

    # Step 3: stop with empty set when already visited
    if drug in visited:
        return set()
    visited.add(drug)

    # Step 6: take direct neighbors, then recursively union their neighbors
    direct = set(interaction_tree.get(drug, set()))
    if not direct:
        return set()

    # Step 7: return accumulated interaction set
    return direct | set().union(
        *(find_medication_interactions(d, interaction_tree, visited) for d in direct)
    )


if __name__ == "__main__":
    print(find_medication_interactions("a", {"a": {"b"}, "b": {"c"}}))
