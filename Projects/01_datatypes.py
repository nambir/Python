"""Slide 3 — Python datatypes (CSV Batch 2 topic 1)."""


def step1_primitives():
    age, price, name, is_student = 25, 99.5, "Ravi", True
    print("primitives:", age, price, name, is_student)


def step2_collections():
    numbers = [10, 20, 30]
    point = (10, 20)
    colors = {"red", "green"}
    frozen = frozenset({"read", "write"})
    student = {"name": "Ravi", "age": 15}
    print("list:", numbers, "tuple:", point, "set:", colors)
    print("frozenset:", frozen, "dict:", student)


def step3_list_index_slice():
    nums = [10, 20, 30, 40]
    print("index:", nums[0], "last:", nums[-1], "slice:", nums[1:3])
    nums.append(50)
    print("after append:", nums)


def step4_tuple_pack_unpack():
    point = (12.97, 80.22)
    lat, lng = point
    print("unpack:", lat, lng)
    try:
        point = (12.97, 80.22)
        point[0] = 15
    except TypeError as e:
        print("tuple immutable:", e)


def step5_set_unique():
    tags = {"python", "code", "python"}
    print("set unique:", tags)


def step6_frozenset():
    perms = frozenset({"read", "write"})
    cache = {perms: "allowed"}
    print("frozenset dict key:", cache)
    try:
        perms.add("admin")
    except AttributeError as e:
        print("frozenset cannot change:", e)


def step7_11_dict_keys():
    grid = {}
    grid[(1, 2)] = "cell"
    try:
        grid[[1, 2]] = "X"
    except TypeError as e:
        print("list key fails:", e)
    try:
        grid[{"id": 1}] = "data"
    except TypeError as e:
        print("dict key fails:", e)


if __name__ == "__main__":
    print("=== Step 1: primitives ===")
    step1_primitives()
    print("\n=== Step 2: collections ===")
    step2_collections()
    print("\n=== Step 3: list index/slice ===")
    step3_list_index_slice()
    print("\n=== Step 4: tuple pack/unpack ===")
    step4_tuple_pack_unpack()
    print("\n=== Step 5: set uniqueness ===")
    step5_set_unique()
    print("\n=== Step 6: frozenset ===")
    step6_frozenset()
    print("\n=== Step 7-11: dict keys ===")
    step7_11_dict_keys()
    print("\n=== Step 13: summary ===")
    print("Dict keys OK: int, str, tuple, frozenset")
    print("Dict keys NOT OK: list, dict, set")
