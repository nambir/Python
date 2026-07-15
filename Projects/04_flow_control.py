"""Slide 4 — Conditional & Flow Control practice."""


def grade_for(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 60:
        return "B"
    return "C"


def fizzbuzz(n: int) -> list[str]:
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def search_with_for_else(items: list[int], target: int) -> str:
    for x in items:
        if x == target:
            return f"found {target}"
    else:
        return "not found"


def demo_pass_and_if_flags():
  """pass, if True, and if False patterns."""
  def not_ready_yet():
    pass  # TODO

  class PendingFeature(Exception):
    pass

  ran_true_block = False
  if True:
    ran_true_block = True
    pass

  ran_false_block = False
  if False:
    ran_false_block = True

  return {
    "stub_callable": callable(not_ready_yet),
    "true_block_entered": ran_true_block,
    "false_block_entered": ran_false_block,
  }


if __name__ == "__main__":
    print("grade 75:", grade_for(75))
    print("fizzbuzz 1-20:", fizzbuzz(20))
    print(search_with_for_else([1, 2, 3], 5))
    print("pass / if flags:", demo_pass_and_if_flags())
