"""Self-contained Review base-concept examples."""

CHUNK = {
    'keyword-only parameters': (
        '# INPUT\ndef record_dose(patient, *, drug, mg):\n    return patient + " gets " + drug + " " + str(mg) + "mg"\n\nprint(record_dose("Asha", drug="Amoxicillin", mg=500))\ntry:\n    record_dose("Asha", "Amoxicillin", 500)\nexcept TypeError:\n    print("TypeError: drug and mg must be passed by name")\n# OUTPUT\nAsha gets Amoxicillin 500mg\nTypeError: drug and mg must be passed by name',
        'Parameters written after a bare * in a function definition are keyword-only: callers must name them, like drug="Amoxicillin". This is useful when a call like record_dose("Asha", "Amoxicillin", 500) would be easy to misread or mix up. Forcing names makes medication code self-documenting and prevents swapping the drug and the dose by accident.',
    ),
    'lambda': (
        '# INPUT\nbmi = lambda kg, m: round(kg / (m * m), 1)\nprint(bmi(70, 1.75))\n\npatients = [("Asha", 38.5), ("Ravi", 37.0)]\npatients.sort(key=lambda p: p[1])\nprint(patients)\n# OUTPUT\n22.9\n[(\'Ravi\', 37.0), (\'Asha\', 38.5)]',
        'A lambda is a tiny unnamed function written in one line: lambda inputs: result. It behaves exactly like a small def, but you can write it right where it is needed. Lambdas shine as short helpers passed to sort, map, or filter, like sorting patients by temperature here. For anything longer than one simple expression, use a normal def so the code stays readable.',
    ),
    'lazy evaluation': (
        '# INPUT\ndef readings():\n    print("producing 1")\n    yield 1\n    print("producing 2")\n    yield 2\n\ngen = readings()\nprint("nothing produced yet")\nprint(next(gen))\n# OUTPUT\nnothing produced yet\nproducing 1\n1',
        'Lazy evaluation means work happens only when the result is actually asked for, not when it is set up. Calling readings() builds a generator but runs none of its body; the first "producing" line appears only when next() demands a value. This is great for huge data, like streaming thousands of patient readings, because you never compute or store values nobody has requested yet.',
    ),
    'list': (
        '# INPUT\ntemps = [36.6, 37.2, 38.5]\nprint(temps[0])\nprint(len(temps))\nprint(38.5 in temps)\n# OUTPUT\n36.6\n3\nTrue',
        "A list is an ordered, changeable collection written with square brackets. You reach items by position starting at 0 (temps[0] is the first reading), count them with len(), and test membership with in. Lists are the go-to container when order matters and the data will grow or change, such as a patient's temperature log over a shift.",
    ),
    'list append': (
        '# INPUT\nward = ["Asha"]\nward.append("Ravi")\nprint(ward)\nresult = ward.append("Meena")\nprint(result)\nprint(ward)\n# OUTPUT\n[\'Asha\', \'Ravi\']\nNone\n[\'Asha\', \'Ravi\', \'Meena\']',
        'append() adds one item to the end of a list, changing the list in place. Note the common beginner trap shown here: append returns None, not the new list, so writing ward = ward.append(...) would destroy your data. Use append when items arrive one at a time, like admitting patients to a ward roster; it is fast because the end of a list is cheap to grow.',
    ),
    'list comprehension': (
        '# INPUT\ntemps_c = [36.6, 38.5, 37.0]\nfevers = [t for t in temps_c if t >= 38.0]\ntemps_f = [round(t * 9 / 5 + 32, 1) for t in temps_c]\nprint(fevers)\nprint(temps_f)\n# OUTPUT\n[38.5]\n[97.9, 101.3, 98.6]',
        'A list comprehension builds a new list in one readable line: [expression for item in source if condition]. The first one filters (keep only fevers), the second transforms (convert every Celsius reading to Fahrenheit). Use comprehensions instead of a for-loop with append when the goal is simply "make a new list from an old one"; they are shorter and state the intent directly.',
    ),
    'list insertion': (
        '# INPUT\nqueue = ["Asha", "Meena"]\nqueue.insert(1, "Ravi")\nprint(queue)\nqueue.insert(0, "URGENT: Devi")\nprint(queue)\n# OUTPUT\n[\'Asha\', \'Ravi\', \'Meena\']\n[\'URGENT: Devi\', \'Asha\', \'Ravi\', \'Meena\']',
        'insert(position, item) places an item at any spot in a list, pushing later items to the right. Here an urgent patient is inserted at position 0, jumping the clinic queue. Be aware inserting near the front is slow on large lists because every item after it must shift; if you insert at the front a lot, a deque (double-ended queue) from collections is the better tool.',
    ),
    'local variables': (
        '# INPUT\ndef check_fever(temp):\n    threshold = 38.0\n    return temp >= threshold\n\nprint(check_fever(38.5))\ntry:\n    print(threshold)\nexcept NameError:\n    print("NameError: threshold only exists inside the function")\n# OUTPUT\nTrue\nNameError: threshold only exists inside the function',
        'A variable created inside a function is local: it is born when the function runs and disappears when the function returns. Outside the function the name does not exist, which is why printing threshold raises NameError. This isolation is a feature: each function keeps its own scratch values, so two functions can both use a name like threshold without interfering with each other.',
    ),
    'loop': (
        '# INPUT\npatients = ["Asha", "Ravi"]\nfor name in patients:\n    print("Checking " + name)\n\ncount = 0\nwhile count < 2:\n    count += 1\nprint("Rounds done:", count)\n# OUTPUT\nChecking Asha\nChecking Ravi\nRounds done: 2',
        'A loop repeats work without copy-pasting code. A for loop visits each item in a collection once, perfect for "do this for every patient". A while loop repeats as long as a condition stays true, useful when you do not know the count in advance, like "keep monitoring until the alarm clears". Prefer for when walking a known collection and while for open-ended repetition.',
    ),
    'map': (
        '# INPUT\ndoses_mg = [250, 500, 750]\ndoses_g = map(lambda mg: mg / 1000, doses_mg)\nprint(doses_g is not doses_mg)\nprint(list(doses_g))\n# OUTPUT\nTrue\n[0.25, 0.5, 0.75]',
        'map(function, collection) applies one function to every item and gives back a lazy map object, a new thing, not the original list. Values are only computed when you consume it, for example with list(). Use map to convert whole datasets in one call, like turning every dose from milligrams to grams. A list comprehension does the same job and many people find it easier to read.',
    ),
    'max': (
        '# INPUT\ntemps = {"Asha": 37.1, "Ravi": 39.2, "Meena": 38.0}\nprint(max(temps.values()))\nprint(max(temps, key=temps.get))\nprint(max([], default="no readings"))\n# OUTPUT\n39.2\nRavi\nno readings',
        'max() returns the largest item. Two extras make it powerful: key= tells it how to rank items, so max(temps, key=temps.get) finds which patient has the highest fever, not just the highest number; and default= gives a safe answer for an empty collection instead of crashing with ValueError. Use default whenever the data might legitimately be empty, like a patient with no readings yet.',
    ),
    'memory complexity': (
        '# INPUT\nimport sys\n\nsmall = list(range(10))\nbig = list(range(10000))\nprint(sys.getsizeof(big) > sys.getsizeof(small))\n\ndef total_lazy(n):\n    total = 0\n    for i in range(n):\n        total += i\n    return total\n\nprint(total_lazy(10000))\n# OUTPUT\nTrue\n49995000',
        'Memory complexity describes how memory needs grow with input size. Building a list of n readings uses O(n) memory: 10000 items take far more space than 10, as the size comparison shows. total_lazy uses O(1) extra memory: it keeps only one running total no matter how large n is, because range produces numbers one at a time. When processing huge patient datasets, prefer the O(1) streaming style if you only need a summary, not the whole list.',
    ),
    'memory overhead': (
        '# INPUT\nimport sys\n\nprint(sys.getsizeof([]) > 0)\nprint(sys.getsizeof([1, 2, 3]) > sys.getsizeof(()))\nprint(sys.getsizeof("A") > 1)\n# OUTPUT\nTrue\nTrue\nTrue',
        'Memory overhead is the extra bookkeeping space Python objects carry beyond the raw data. Even an empty list takes real bytes, and a one-character string uses far more than 1 byte, because every object stores its type, reference count, and other housekeeping. Exact byte counts differ between Python versions, so this example prints stable comparisons instead of raw numbers. Overhead matters when you store millions of tiny records, where specialized structures can save a lot.',
    ),
    'memory profiling': (
        '# INPUT\nimport tracemalloc\n\ntracemalloc.start()\nrecords = [{"id": i, "temp": 37.0} for i in range(1000)]\ncurrent, peak = tracemalloc.get_traced_memory()\ntracemalloc.stop()\n\nprint(len(records))\nprint(current > 0)\nprint(peak >= current)\n# OUTPUT\n1000\nTrue\nTrue',
        'Memory profiling means measuring how much memory your code actually allocates, rather than guessing. The built-in tracemalloc module records allocations between start() and stop(): current is memory still held, peak is the highest point reached. Exact byte numbers vary by machine and Python version, so we print stable facts (current is positive, peak is at least current). Profile before optimizing, so you fix the real memory hog, for example a hospital report building giant lists.',
    ),
    'memory use': (
        '# INPUT\nimport sys\n\nfew = [37.0] * 10\nmany = [37.0] * 10000\nprint(sys.getsizeof(many) > sys.getsizeof(few))\n\nas_list = list(range(100000))\nas_range = range(100000)\nprint(sys.getsizeof(as_list) > sys.getsizeof(as_range))\n# OUTPUT\nTrue\nTrue',
        'sys.getsizeof(obj) reports how many bytes an object itself occupies. Bigger lists use more memory, but the second comparison is the interesting one: a range of 100000 numbers is tiny because it stores only start, stop, and step, while the equivalent list stores every number. Exact sizes vary by interpreter, so we print comparisons, not raw counts. Choosing lazy objects like range over materialized lists is one of the easiest ways to cut memory use.',
    ),
    'missing data': (
        '# INPUT\npatient = {"name": "Asha", "temp": None}\nprint(patient.get("blood_type"))\nprint(patient.get("blood_type", "unknown"))\nif patient["temp"] is None:\n    print("temp not recorded yet")\n# OUTPUT\nNone\nunknown\ntemp not recorded yet',
        'Real records often have gaps: a field may be absent entirely, or present but set to None (recorded as "not measured yet"). dict.get() handles absent keys without crashing and can supply a default like "unknown". Compare against None with is None. Handling missing data explicitly is essential in healthcare code, where treating "no reading" as 0 could look like a dangerously low temperature.',
    ),
    'mutability': (
        '# INPUT\nallergies = ["penicillin"]\nallergies.append("latex")\nprint(allergies)\n\nname = "asha"\nupper = name.upper()\nprint(name)\nprint(upper)\n# OUTPUT\n[\'penicillin\', \'latex\']\nasha\nASHA',
        'Mutability is whether an object can be changed after creation. Lists are mutable: append really modifies the allergy list. Strings are immutable: upper() cannot change "asha", so it returns a brand new string and the original stays intact. Knowing which types mutate (list, dict, set) and which never do (str, int, tuple) explains many surprises, like why editing one variable sometimes affects another.',
    ),
    'mutable objects': (
        '# INPUT\nchart_a = ["ibuprofen"]\nchart_b = chart_a\nchart_b.append("aspirin")\nprint(chart_a)\nprint(chart_a is chart_b)\n\nsafe_copy = list(chart_a)\nsafe_copy.append("codeine")\nprint(chart_a)\nprint(safe_copy)\n# OUTPUT\n[\'ibuprofen\', \'aspirin\']\nTrue\n[\'ibuprofen\', \'aspirin\']\n[\'ibuprofen\', \'aspirin\', \'codeine\']',
        'Assignment never copies a mutable object; chart_b = chart_a makes both names point at the same list, so appending through one is visible through the other (is confirms they are the same object). To edit independently, make a real copy first with list(...) or .copy(). This matters whenever two parts of a program share data, for example two screens showing the same medication chart.',
    ),
    'mutation': (
        '# INPUT\ndef add_med_bad(med, meds=[]):\n    meds.append(med)\n    return meds\n\nprint(add_med_bad("a"))\nprint(add_med_bad("b"))\n\ndef add_med_good(med, meds=None):\n    if meds is None:\n        meds = []\n    meds.append(med)\n    return meds\n\nprint(add_med_good("a"))\nprint(add_med_good("b"))\n# OUTPUT\n[\'a\']\n[\'a\', \'b\']\n[\'a\']\n[\'b\']',
        'Mutation is changing an object in place, and it can bite when objects are shared. The classic trap: a mutable default like meds=[] is created once and reused for every call, so patient "b" mysteriously inherits patient "a"\'s medication. The fix is the meds=None pattern, which builds a fresh list per call. Rule of thumb: never use a mutable value as a default argument.',
    ),
    'mypy': (
        '# INPUT\nsource = (\n    "def dose_for_weight(kg: float) -> float:\\n"\n    "    return kg * 10\\n"\n    "\\n"\n    "dose_for_weight(\'70\')  # wrong type on purpose"\n)\nprint(source)\nprint("---")\nprint("Illustrative mypy result (mypy is a separate tool, not run by Python):")\nprint(\'error: Argument 1 to "dose_for_weight" has incompatible type "str"; expected "float"\')\n# OUTPUT\ndef dose_for_weight(kg: float) -> float:\n    return kg * 10\n\ndose_for_weight(\'70\')  # wrong type on purpose\n---\nIllustrative mypy result (mypy is a separate tool, not run by Python):\nerror: Argument 1 to "dose_for_weight" has incompatible type "str"; expected "float"',
        'mypy is a static type checker: a separate command-line tool (run as "mypy yourfile.py"), not part of the Python runtime. It reads your type hints and reports mismatches before the program ever runs; Python itself would happily start this code and only fail later. Here the snippet is held in a string and the checker message shown is illustrative of what mypy prints. Use mypy in medical software to catch bugs like passing a weight as text instead of a number.',
    ),
    'nested conditions': (
        '# INPUT\ntemp = 39.0\nage = 4\nif temp >= 38.0:\n    if age < 5:\n        print("fever in young child: see doctor today")\n    else:\n        print("fever: rest and fluids")\nelse:\n    print("no fever")\n# OUTPUT\nfever in young child: see doctor today',
        'A nested condition is an if inside another if: the inner question is only asked when the outer answer is yes. Here we first check for fever, and only then ask whether the patient is a young child, mirroring how triage decisions actually branch. Keep nesting shallow (two or three levels); deeper trees are hard to follow and can often be flattened with and, or by returning early from a function.',
    ),
    'nested dictionaries': (
        '# INPUT\npatients = {\n    "P001": {"name": "Asha", "vitals": {"temp": 38.5, "pulse": 92}},\n}\nprint(patients["P001"]["vitals"]["temp"])\nprint(patients.get("P999", {}).get("name", "not found"))\n# OUTPUT\n38.5\nnot found',
        'A nested dictionary is a dict whose values are themselves dicts, ideal for record-like data: patient id maps to a record, which contains a vitals sub-record. You drill down by chaining keys: patients["P001"]["vitals"]["temp"]. For possibly-missing data, chain .get() with a {} default so a missing patient gives "not found" instead of a KeyError crash.',
    ),
    'nested functions': (
        '# INPUT\ndef make_alert(ward):\n    def alert(patient):\n        return "[" + ward + "] check " + patient\n    return alert\n\nicu_alert = make_alert("ICU")\nprint(icu_alert("Asha"))\nprint(icu_alert("Ravi"))\n# OUTPUT\n[ICU] check Asha\n[ICU] check Ravi',
        "A nested function is defined inside another function. The inner alert() can use the outer function's variable ward even after make_alert has finished; this remembered environment is called a closure. It lets you build customized functions from a template: one factory call produces an ICU-specific alert function you can reuse for every patient. Use nesting for small helpers that only make sense inside their parent, or for factories like this.",
    ),
    'nested loops': (
        '# INPUT\nwards = ["ICU", "ER"]\nshifts = ["day", "night"]\nfor ward in wards:\n    for shift in shifts:\n        print(ward, shift)\n# OUTPUT\nICU day\nICU night\nER day\nER night',
        'A nested loop is a loop inside a loop: for every item of the outer loop, the inner loop runs completely. That produces every combination, here every ward paired with every shift for a duty roster. Watch the cost: the total work is outer times inner (2 x 2 = 4 here), so nesting two loops over big lists multiplies quickly, which is why nested loops over large data are a common performance problem.',
    ),
    'next': (
        '# INPUT\nreadings = iter([37.0, 38.5])\nprint(next(readings))\nprint(next(readings))\nprint(next(readings, "no more readings"))\n# OUTPUT\n37.0\n38.5\nno more readings',
        'next(iterator) hands you the next value from an iterator, one at a time, remembering position between calls. When values run out, next raises StopIteration unless you give a second argument as a fallback, like "no more readings" here. Use next when you want just one item, like the first patient matching a condition from a generator, without looping over everything.',
    ),
    'nonlocal': (
        '# INPUT\ndef make_counter():\n    count = 0\n    def visit():\n        nonlocal count\n        count += 1\n        return count\n    return visit\n\nvisits = make_counter()\nprint(visits())\nprint(visits())\n# OUTPUT\n1\n2',
        'nonlocal lets an inner function modify a variable that belongs to its enclosing function, not create its own local copy. Without the nonlocal line, count += 1 would fail with UnboundLocalError because Python would treat count as a brand new local variable. This enables lightweight stateful helpers, like a visit counter per clinic room, without needing a class or a global variable.',
    ),
    'normalization': (
        '# INPUT\nraw_names = ["  ASHA ", "asha", "Asha  "]\nnormalized = [n.strip().lower() for n in raw_names]\nprint(normalized)\nprint(len(set(normalized)))\n# OUTPUT\n[\'asha\', \'asha\', \'asha\']\n1',
        'Normalization means converting data to one standard form before comparing or storing it. Three differently-typed versions of the same patient name become identical after strip() removes stray spaces and lower() unifies the case, so the set collapses them to 1 unique name. Always normalize user-entered data first; otherwise "ASHA" and "asha" look like two different patients and you get duplicate records.',
    ),
    'not in': (
        '# INPUT\nallergies = ["penicillin", "latex"]\ndrug = "ibuprofen"\nif drug not in allergies:\n    print("safe to prescribe ibuprofen")\nprint("aspirin" not in allergies)\n# OUTPUT\nsafe to prescribe ibuprofen\nTrue',
        'not in tests that a value is absent from a collection, returning True or False. It reads like English, which makes safety checks clear: "if drug not in allergies" is exactly the question a prescriber asks. It works on lists, strings, sets, and dict keys. Prefer x not in items over not (x in items); both work but the first is the idiomatic, readable form.',
    ),
    'object identity': (
        '# INPUT\na = ["Asha"]\nb = ["Asha"]\nc = a\nprint(a == b)\nprint(a is b)\nprint(a is c)\n# OUTPUT\nTrue\nFalse\nTrue',
        'Identity asks "are these the very same object in memory?" while equality (==) asks "do they hold the same value?". Two separately-built lists are equal but not identical; c = a just adds a second name for one object, so a is c. Use is almost exclusively for is None checks; use == for comparing values. Confusing the two causes subtle bugs, especially with mutable objects that several names share.',
    ),
    'object lifetime': (
        '# INPUT\nclass Monitor:\n    def __init__(self, patient):\n        self.patient = patient\n        print("monitor attached to " + patient)\n    def __del__(self):\n        print("monitor released")\n\nm = Monitor("Asha")\nm = None\nprint("done")\n# OUTPUT\nmonitor attached to Asha\nmonitor released\ndone',
        'An object lives from its creation until nothing refers to it anymore, then Python reclaims its memory. Rebinding m to None removes the last reference, so the Monitor is destroyed and __del__ runs before "done" prints. Note this immediate cleanup is how CPython (reference counting) behaves; other Python implementations may delay it. For critical resources like files or device connections, do not rely on __del__; use a with block instead.',
    ),
    'object memory': (
        '# INPUT\nimport sys\n\nprint(sys.getsizeof(1) > 0)\nprint(sys.getsizeof("Asha Kumar") > sys.getsizeof("A"))\nprint(sys.getsizeof([1, 2, 3]) >= sys.getsizeof([]))\n# OUTPUT\nTrue\nTrue\nTrue',
        'Every Python value is an object with real memory cost: even the integer 1 occupies dozens of bytes because it carries type information and a reference count alongside the number itself. Longer strings and fuller lists take more space than short or empty ones. Exact byte counts change between Python versions, so this example prints comparisons rather than raw numbers. This per-object cost is why storing millions of readings sometimes needs compact tools like arrays.',
    ),
    'opaque identifiers': (
        '# INPUT\nimport uuid\n\npatient_id = "P-7f3a"\nrecord = {patient_id: {"name": "Asha", "temp": 38.5}}\nprint(record["P-7f3a"]["name"])\n\nfixed = uuid.UUID("12345678-1234-5678-1234-567812345678")\nprint(str(fixed))\n# OUTPUT\nAsha\n12345678-1234-5678-1234-567812345678',
        'An opaque identifier is an ID that deliberately reveals nothing about what it labels: "P-7f3a" says nothing about Asha\'s name, age, or condition. That protects privacy and stays stable even if the person\'s details change. UUIDs (universally unique identifiers) are a standard way to generate such IDs; normally you would call uuid.uuid4() for a random one, but this example builds a fixed UUID so the printed output is stable.',
    ),
    'optional values': (
        '# INPUT\nfrom typing import Optional\n\ndef find_temp(records: dict, pid: str) -> Optional[float]:\n    return records.get(pid)\n\nrecords = {"P001": 38.5}\ntemp = find_temp(records, "P002")\nif temp is None:\n    print("no reading for P002")\nprint(find_temp(records, "P001"))\n# OUTPUT\nno reading for P002\n38.5',
        'An optional value is one that might legitimately be absent, represented in Python by None. The type hint Optional[float] documents that find_temp returns either a temperature or None when the patient has no reading. Always check is None before using such a value; forgetting is a top source of crashes ("NoneType has no attribute..."). Modern Python also allows writing the same hint as float | None.',
    ),
    'parentheses': (
        '# INPUT\nprint(2 + 3 * 4)\nprint((2 + 3) * 4)\n\nsingle = (37.0)\nreal_single = (37.0,)\nprint(type(single).__name__)\nprint(type(real_single).__name__)\n# OUTPUT\n14\n20\nfloat\ntuple',
        'Parentheses do two different jobs. First, they group math to override precedence: (2 + 3) * 4 forces the addition first. Second, they appear around tuples, but the comma, not the parentheses, makes the tuple: (37.0) is just the number 37.0, while (37.0,) with a trailing comma is a one-item tuple. When a formula encodes something important like a dosage, add parentheses even when optional; they make intent unmistakable.',
    ),
    'positional-only parameters': (
        '# INPUT\ndef bmi(kg, m, /):\n    return round(kg / (m * m), 1)\n\nprint(bmi(70, 1.75))\ntry:\n    bmi(kg=70, m=1.75)\nexcept TypeError:\n    print("TypeError: kg and m must be positional")\n# OUTPUT\n22.9\nTypeError: kg and m must be positional',
        'Parameters before a / in a function definition are positional-only: callers cannot use their names, so bmi(kg=70, m=1.75) raises TypeError. This is the mirror image of keyword-only parameters (marked with *). Library authors use / so they can rename internal parameters later without breaking callers, and many builtins like len() work this way. In everyday code you will mostly read this syntax rather than write it.',
    ),
    'precedence': (
        '# INPUT\nprint(2 + 3 * 4)\nprint(not True == False)\n\ntemp = 39.0\non_meds = False\nprint(temp > 38.0 and not on_meds)\n# OUTPUT\n14\nTrue\nTrue',
        'Precedence is the order Python applies operators: multiplication before addition (so 2 + 3 * 4 is 14, not 20), comparisons before not, and not before and/or. That is why not True == False means not (True == False), which is True. Misreading precedence in a clinical rule could flip a treatment decision, so when a condition mixes not, and, and comparisons, add parentheses to state the order explicitly.',
    ),
    'primary keys': (
        '# INPUT\npatients = {\n    "P001": {"name": "Asha"},\n    "P002": {"name": "Asha"},\n}\nprint(patients["P002"]["name"])\nprint(len(patients))\npatients["P001"] = {"name": "Asha K."}\nprint(patients["P001"]["name"])\n# OUTPUT\nAsha\n2\nAsha K.',
        "A primary key is a unique identifier for each record, the concept behind dict keys here. Two patients can share the name Asha, but their IDs P001 and P002 keep the records separate, which is why hospitals never look people up by name alone. The key stays fixed for the record's lifetime while the data under it can be updated. Choose keys that never change and never repeat, like an assigned patient ID.",
    ),
    'pyright': (
        '# INPUT\nsource = (\n    "def heart_rate_status(bpm: int) -> str:\\n"\n    "    return \'high\' if bpm > 100 else \'normal\'\\n"\n    "\\n"\n    "heart_rate_status(\'95\')  # wrong type on purpose"\n)\nprint(source)\nprint("---")\nprint("Illustrative pyright result (pyright is a separate tool, not run by Python):")\nprint(\'error: Argument of type "str" cannot be assigned to parameter "bpm" of type "int"\')\n# OUTPUT\ndef heart_rate_status(bpm: int) -> str:\n    return \'high\' if bpm > 100 else \'normal\'\n\nheart_rate_status(\'95\')  # wrong type on purpose\n---\nIllustrative pyright result (pyright is a separate tool, not run by Python):\nerror: Argument of type "str" cannot be assigned to parameter "bpm" of type "int"',
        "pyright is a fast static type checker from Microsoft; it powers the type errors you see in VS Code via Pylance. Like mypy, it is a separate tool run on your source files, not part of the Python runtime: Python would run this snippet without complaint until something breaks. The snippet is held in a string and the error message shown is illustrative of pyright's output. Checkers like this catch type mistakes, such as a heart rate passed as text, before the code ships.",
    ),
    'recursion': (
        '# INPUT\ndef count_down_checks(n):\n    if n == 0:\n        return "all patients checked"\n    print("checking patient", n)\n    return count_down_checks(n - 1)\n\nprint(count_down_checks(3))\n# OUTPUT\nchecking patient 3\nchecking patient 2\nchecking patient 1\nall patients checked',
        'Recursion is a function calling itself, each time on a smaller version of the problem. Two parts are essential: a base case that stops (n == 0 returns the final message) and a step that shrinks the problem (n - 1). Without a base case you get RecursionError. Recursion is natural for nested structures like organizational charts or folder trees; for a simple countdown like this, a loop is equally fine and uses less memory.',
    ),
    'reduce': (
        '# INPUT\nfrom functools import reduce\n\ndoses = [250, 500, 250]\ntotal = reduce(lambda a, b: a + b, doses)\nprint(total)\nprint(reduce(lambda a, b: a + b, [], 0))\n# OUTPUT\n1000\n0',
        'reduce folds a whole list into one value by repeatedly applying a two-argument function: ((250 + 500) + 250) = 1000, the total daily dose. The optional third argument is a starting value, which also makes reduce safe on an empty list (it just returns 0) instead of raising TypeError. For plain addition prefer the builtin sum(); reach for reduce when combining with a custom rule that has no builtin.',
    ),
    'reference counting': (
        '# INPUT\nimport sys\n\nchart = ["med list"]\ncount_1 = sys.getrefcount(chart)\nalias = chart\ncount_2 = sys.getrefcount(chart)\nprint(count_2 == count_1 + 1)\ndel alias\nprint(sys.getrefcount(chart) == count_1)\n# OUTPUT\nTrue\nTrue',
        "CPython keeps a reference count for every object: how many names or containers currently point to it. Creating the alias raises the count by one; del alias drops it back. When the count hits zero the object's memory is freed immediately, which is how object lifetime works in CPython. We print comparisons because getrefcount's absolute number includes temporary references and varies; the +1 relationship is the stable, meaningful part.",
    ),
    'required fields': (
        '# INPUT\ndef register(record):\n    required = ["name", "dob"]\n    missing = [f for f in required if f not in record]\n    if missing:\n        return "missing required fields: " + ", ".join(missing)\n    return "registered " + record["name"]\n\nprint(register({"name": "Asha", "dob": "2000-01-01"}))\nprint(register({"name": "Ravi"}))\n# OUTPUT\nregistered Asha\nmissing required fields: dob',
        'Required fields are the pieces of data a record must contain before it is accepted, like name and date of birth on a patient registration. The pattern here builds a list of whatever is missing and reports it all at once, which is friendlier than failing on the first gap. Validate at the boundary where data enters your system, so everything deeper in the program can trust the record is complete.',
    ),
}
