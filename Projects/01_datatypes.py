"""Slide 5 — Python datatypes: realistic list/tuple usage."""
import sys


def demo_lists():
    scores = [90, 85, 88]
    vendors = ["Google", "Amazon", "Azure"]
    order = [101, "SHIPPED", ["Google", "Amazon"]]
    print("homogeneous ints:", scores)
    print("homogeneous strs:", vendors)
    print("heterogeneous:", order)
    print("nested vendor:", order[2][0])


def demo_list_memory():
    print("\n--- list memory growth (watch sizeof jump) ---")
    cart = []
    print(f"len=0  sizeof={sys.getsizeof(cart)}")
    for i in range(12):
        cart.append(i)
        print(f"len={len(cart):2d}  sizeof={sys.getsizeof(cart)}")


def demo_tuple_real():
    lat_lng = (12.9716, 80.2212)
    rgb = (255, 128, 0)
    employee = ("E102", "Anu", 75000)

    def fetch_user(user_id):
        if user_id < 0:
            return False, None
        return True, {"id": user_id, "name": "Anu"}

    ok, user = fetch_user(10)
    cache = {("orders", 2026, 7): 42}
    print("\n--- tuple real uses ---")
    print("GPS:", lat_lng)
    print("RGB:", rgb)
    print("employee:", employee)
    print("fetch:", ok, user)
    print("dict key:", cache)


def demo_tuple_vs_list_size():
    a_list = [1, 2, 3]
    a_tuple = (1, 2, 3)
    print("\n--- memory: list vs tuple (same 3 ints) ---")
    print("list  bytes:", sys.getsizeof(a_list))
    print("tuple bytes:", sys.getsizeof(a_tuple))


def demo_why_immutable_keys():
    print("\n--- why dict keys must be immutable ---")
    prices = {}
    prices["apple"] = 40
    prices[(12.97, 80.22)] = "Chennai warehouse"
    print("OK str + tuple keys:", prices)

    try:
        prices[[12.97, 80.22]] = "fail"
    except TypeError as e:
        print("list as key:", e)

    try:
        prices[{"city": "Chennai"}] = "fail"
    except TypeError as e:
        print("dict as key:", e)

    # Thought experiment printed as comments for learners:
    print("If list keys were allowed and you mutated the list,")
    print("hash would change and the value could not be found again.")


if __name__ == "__main__":
    demo_lists()
    demo_list_memory()
    demo_tuple_real()
    demo_tuple_vs_list_size()
    demo_why_immutable_keys()
