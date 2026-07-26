"""Self-contained Review base-concept examples."""

CHUNK = {
    'defaults': (
        "# INPUT\ndef dose_label(drug, unit='mg'):\n    return f'{drug} ({unit})'\nprint(dose_label('aspirin'))\nprint(dose_label('insulin', 'units'))\n\n# OUTPUT\naspirin (mg)\ninsulin (units)",
        'A default is a preset parameter value used when the caller omits that argument. Use defaults for common cases so call sites stay short, and override only when needed.',
    ),
    'defensive copying': (
        "# INPUT\nincoming = ['fever', 'cough']\nchart = list(incoming)\nincoming.append('rash')\nprint(chart)\nprint(incoming)\n\n# OUTPUT\n['fever', 'cough']\n['fever', 'cough', 'rash']",
        "Defensive copying stores a new list (or other container) instead of keeping the caller's object. Do this when outside code might mutate the input later and you need a stable copy.",
    ),
    'deque': (
        "# INPUT\nfrom collections import deque\ntriage = deque(['A1', 'A2'])\ntriage.appendleft('STAT')\nprint(triage.popleft())\nprint(list(triage))\n\n# OUTPUT\nSTAT\n['A1', 'A2']",
        'A deque (double-ended queue) adds and removes quickly at both ends. Use it for queues, triage lines, or any FIFO/LIFO work where list.insert(0, ...) would be slow.',
    ),
    'dict': (
        "# INPUT\npatient = {'id': 'P42', 'ward': 'ICU'}\nprint(patient['ward'])\nprint(patient)\n\n# OUTPUT\nICU\n{'id': 'P42', 'ward': 'ICU'}",
        'A dict maps keys to values for fast named lookup. Use it when each item has a label (id, ward, dose) rather than only a position.',
    ),
    'dict comprehension': (
        "# INPUT\ncodes = ['BP', 'HR', 'Temp']\nunits = {c: 'mmHg' if c == 'BP' else 'bpm' if c == 'HR' else 'C' for c in codes}\nprint(units)\n\n# OUTPUT\n{'BP': 'mmHg', 'HR': 'bpm', 'Temp': 'C'}",
        'A dict comprehension builds a dictionary in one expression from a loop. Use it when each key/value pair follows a clear rule and a full for-loop would be longer.',
    ),
    'dict keys': (
        "# INPUT\nvitals = {'BP': 120, 'HR': 72}\nprint(list(vitals.keys()))\nprint('HR' in vitals)\n\n# OUTPUT\n['BP', 'HR']\nTrue",
        'Dict keys are the names used to find values. Loop keys, test membership with in, or call .keys() when you need the key collection itself.',
    ),
    'dict.get': (
        "# INPUT\nrecord = {'name': 'Mia'}\nprint(record.get('allergy', 'none'))\nprint(record.get('name', 'none'))\n\n# OUTPUT\nnone\nMia",
        'dict.get(key, default) returns the value or a fallback instead of raising KeyError. Use it for optional fields (allergy, email) where missing data is expected.',
    ),
    'dictionary lookup': (
        "# INPUT\nmenu = {'tea': 2.5, 'coffee': 3.0}\nprint(menu['tea'])\n\n# OUTPUT\n2.5",
        'Dictionary lookup finds a value by key with average O(1) time. Use [] when the key must exist; prefer .get when absence is normal.',
    ),
    'dictionary return values': (
        "# INPUT\ndef check_dose(mg):\n    return {'ok': mg <= 500, 'mg': mg}\nprint(check_dose(250))\n\n# OUTPUT\n{'ok': True, 'mg': 250}",
        'A function can return a dictionary of related named results. Use this when callers need more than one value (status plus details) without inventing a class.',
    ),
    'division by zero': (
        "# INPUT\ntry:\n    print(10 / 0)\nexcept ZeroDivisionError as e:\n    print(type(e).__name__ + ': ' + str(e))\n\n# OUTPUT\nZeroDivisionError: division by zero",
        'Dividing by zero is undefined and raises ZeroDivisionError. Guard with an if check, or catch the error, whenever a divisor may be zero (ratios, rates).',
    ),
    'domain validation': (
        "# INPUT\ndef set_age(years):\n    if years < 0 or years > 130:\n        raise ValueError('age out of range')\n    return years\ntry:\n    print(set_age(-3))\nexcept ValueError as e:\n    print(type(e).__name__ + ': ' + str(e))\n\n# OUTPUT\nValueError: age out of range",
        'Domain validation checks that values make sense for the real problem (age, dose, temperature). Reject bad input early with a clear error so later logic never runs on nonsense data.',
    ),
    'dynamic arrays': (
        "# INPUT\nbeds = ['101', '102']\nbeds.append('103')\nprint(beds)\nprint(len(beds))\n\n# OUTPUT\n['101', '102', '103']\n3",
        'A Python list is a dynamic array: it grows as you append. Most appends are cheap; occasional resizes copy into a larger block behind the scenes.',
    ),
    'empty collections': (
        "# INPUT\nmeds = []\nnotes = {}\nprint(bool(meds))\nprint(bool(notes))\nprint('empty' if not meds else 'has items')\n\n# OUTPUT\nFalse\nFalse\nempty",
        'Empty lists, dicts, sets, and tuples are false in boolean checks. Use if not items: to handle the no-data case before looping or indexing.',
    ),
    'empty list': (
        '# INPUT\nqueue = []\nprint(queue)\nprint(len(queue))\n\n# OUTPUT\n[]\n0',
        'An empty list is a list with zero items, written []. Start with [] when you will append results as you discover them.',
    ),
    'empty tuple': (
        '# INPUT\ncoords = ()\nprint(coords)\nprint(type(coords).__name__)\n\n# OUTPUT\n()\ntuple',
        'An empty tuple is (), an immutable sequence with no items. Use it as a fixed empty return or default when the collection must never grow.',
    ),
    'enumerate': (
        "# INPUT\nsteps = ['wash', 'glove', 'draw']\nfor i, step in enumerate(steps, start=1):\n    print(f'{i}:{step}')\n\n# OUTPUT\n1:wash\n2:glove\n3:draw",
        'enumerate pairs each item with its index while you loop. Use it when you need both position and value without managing a manual counter.',
    ),
    'equality': (
        '# INPUT\na = [120, 80]\nb = [120, 80]\nprint(a == b)\nprint(a == [120, 81])\n\n# OUTPUT\nTrue\nFalse',
        'Equality (==) asks whether two values have the same contents. Use == for numbers, text, and collections when you care about value, not object identity.',
    ),
    'equality methods': (
        '# INPUT\nclass Dose:\n    def __init__(self, mg):\n        self.mg = mg\n    def __eq__(self, other):\n        return isinstance(other, Dose) and self.mg == other.mg\nprint(Dose(5) == Dose(5))\nprint(Dose(5) == Dose(10))\n\n# OUTPUT\nTrue\nFalse',
        '__eq__ tells a class what equal means for its instances. Define it when objects should compare by fields (dose amount) instead of identity.',
    ),
    'exhaustion': (
        "# INPUT\nit = iter([1, 2])\nprint(next(it))\nprint(next(it))\ntry:\n    print(next(it))\nexcept StopIteration:\n    print('StopIteration')\n\n# OUTPUT\n1\n2\nStopIteration",
        'An iterator is exhausted when no values remain; next then raises StopIteration. A for-loop handles this for you; do not reuse a spent iterator expecting a restart.',
    ),
    'expression grouping': (
        '# INPUT\nprint(2 + 3 * 4)\nprint((2 + 3) * 4)\n\n# OUTPUT\n14\n20',
        'Parentheses group parts of an expression so that part runs first. Use them whenever precedence might confuse readers (dose formulas, score weights).',
    ),
    'filter': (
        '# INPUT\ntemps = [36.5, 38.2, 37.0, 39.1]\nfever = list(filter(lambda t: t >= 38.0, temps))\nprint(fever)\n\n# OUTPUT\n[38.2, 39.1]',
        'filter keeps only items that pass a test function. Convert to list (or loop) to see results; a list comprehension is often clearer for beginners.',
    ),
    'fixed-size C# int': (
        '# INPUT\nbig = 2 ** 100\nprint(big)\nprint(type(big).__name__)\n\n# OUTPUT\n1267650600228229401496703205376\nint',
        'C# int is a fixed bit width and can overflow; Python int grows as needed. Large lab IDs or combinatorial counts stay exact without switching to BigInteger.',
    ),
    'flags': (
        '# INPUT\nis_fasting = True\nis_pregnant = False\nprint(is_fasting and not is_pregnant)\n\n# OUTPUT\nTrue',
        'Flags are small True/False markers that remember a state (fasting, saved, approved). Use clear boolean names so conditions read like English.',
    ),
    'floor division': (
        '# INPUT\ntablets = 25\nper_day = 10\nprint(tablets // per_day)\nprint(tablets / per_day)\n\n# OUTPUT\n2\n2.5',
        'Floor division (//) divides and rounds down to a whole number. Use it for whole packs, pages, or full doses when a fractional leftover must be dropped.',
    ),
    'for loops': (
        "# INPUT\nwards = ['A', 'B', 'C']\nfor w in wards:\n    print('ward ' + w)\n\n# OUTPUT\nward A\nward B\nward C",
        'A for loop repeats once for each item in a sequence. Prefer for when you already have the collection; use while when the stop condition is open-ended.',
    ),
    'function parameters': (
        "# INPUT\ndef label(patient_id, ward):\n    return patient_id + '@' + ward\nprint(label('P9', 'ICU'))\n\n# OUTPUT\nP9@ICU",
        'Parameters are the named inputs a function receives. They turn a function into a reusable recipe: pass different arguments to get different results.',
    ),
    'function signatures': (
        '# INPUT\ndef bmi(weight_kg: float, height_m: float) -> float:\n    return weight_kg / (height_m * height_m)\nprint(round(bmi(70, 1.75), 1))\n\n# OUTPUT\n22.9',
        'A function signature shows the name, parameters, and often return type. Readers and type checkers use it as a contract before reading the body.',
    ),
    'functional operations': (
        "# INPUT\nnames = ['mia', 'sam']\nprint(list(map(str.upper, names)))\nprint([n.upper() for n in names])\n\n# OUTPUT\n['MIA', 'SAM']\n['MIA', 'SAM']",
        'Functional operations transform or select data by passing functions (map, filter, sorted key). Use them for short pipelines; comprehensions are a common, readable alternative.',
    ),
    'generator expression': (
        '# INPUT\ndoses = [5, 10, 15]\ngen = (d * 2 for d in doses)\nprint(next(gen))\nprint(list(gen))\n\n# OUTPUT\n10\n[20, 30]',
        'A generator expression uses (...) to make values one at a time without building a full list. Use it for large or streamed data when you only need to walk the results once.',
    ),
    'generator frame': (
        '# INPUT\ndef countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\ng = countdown(3)\nprint(next(g))\nprint(next(g))\nprint(next(g))\n\n# OUTPUT\n3\n2\n1',
        'A generator frame stores local variables and the pause point between yields. That is why countdown remembers n across next calls without restarting from scratch.',
    ),
    'generators': (
        "# INPUT\ndef vitals():\n    yield 'BP'\n    yield 'HR'\nprint(list(vitals()))\n\n# OUTPUT\n['BP', 'HR']",
        'A generator function uses yield to produce values lazily, one at a time. Use generators for streams, large files, or pipelines where storing everything at once is wasteful.',
    ),
    'global': (
        '# INPUT\ncount = 0\ndef bump():\n    global count\n    count += 1\nbump()\nprint(count)\n\n# OUTPUT\n1',
        'The global statement tells a function to assign to a module-level name. Without it, count += 1 would create a local and raise UnboundLocalError. Prefer returning values when you can.',
    ),
    'global variables': (
        "# INPUT\nHOSPITAL = 'City Care'\ndef banner():\n    return 'Welcome to ' + HOSPITAL\nprint(banner())\n\n# OUTPUT\nWelcome to City Care",
        'Global variables live at module scope and can be read from many functions. Fine for constants; avoid mutable globals for changing state because bugs become hard to trace.',
    ),
    'graphs': (
        "# INPUT\nwards = {'ICU': ['Lab', 'OR'], 'Lab': ['ICU'], 'OR': ['ICU']}\nprint(wards['ICU'])\nprint('Lab' in wards['ICU'])\n\n# OUTPUT\n['Lab', 'OR']\nTrue",
        'A graph models things (nodes) and links between them (edges). Dicts of neighbor lists are a simple way to store hospital routes, referrals, or friendships.',
    ),
    'hash': (
        '# INPUT\nprint(hash(42))\nprint(hash(42) == hash(42))\n\n# OUTPUT\n42\nTrue',
        'hash(value) turns a hashable object into an integer used for quick dict/set placement. Equal immutable values share a stable hash within a run; do not rely on str hashes across processes.',
    ),
    'hash table': (
        "# INPUT\nindex = {}\nindex['P42'] = 'Mia'\nprint(index['P42'])\nprint(len(index))\n\n# OUTPUT\nMia\n1",
        'A hash table stores key-value pairs for fast average lookup. Python dict and set are hash tables; use them when you look up by id far more than by position.',
    ),
    'hashability': (
        "# INPUT\nok = {(10.0, 20.0): 'scan'}\nprint(ok[(10.0, 20.0)])\ntry:\n    bad = {[10.0, 20.0]: 'scan'}\nexcept TypeError as e:\n    print(type(e).__name__ + ': ' + str(e))\n\n# OUTPUT\nscan\nTypeError: unhashable type: 'list'",
        'Only hashable (immutable) values can be dict keys or set members. Tuples of numbers work; lists do not, because their contents can change.',
    ),
    'hashable objects': (
        "# INPUT\nseen = set()\nseen.add('P42')\nseen.add(('lab', 3))\nprint('P42' in seen)\nprint(('lab', 3) in seen)\n\n# OUTPUT\nTrue\nTrue",
        'Hashable objects have a stable hash and can live in sets or be dict keys. Strings, numbers, and tuples of hashables qualify; lists and dicts do not.',
    ),
    'higher-order functions': (
        "# INPUT\npatients = ['Alexandra', 'Jo', 'Sam']\nprint(sorted(patients, key=len))\n\n# OUTPUT\n['Jo', 'Sam', 'Alexandra']",
        'A higher-order function takes or returns another function. sorted(..., key=len) is common: pass a function that extracts the sort key.',
    ),
    'identity value': (
        '# INPUT\ntotal = 0\nfor n in [2, 5, 3]:\n    total += n\nprint(total)\n\n# OUTPUT\n10',
        'An identity value is the starting point that leaves a combining operation unchanged (0 for +, 1 for *). Initialize accumulators with the right identity before looping.',
    ),
    'if/elif/else': (
        "# INPUT\nhr = 45\nif hr < 60:\n    label = 'low'\nelif hr > 100:\n    label = 'high'\nelse:\n    label = 'normal'\nprint(label)\n\n# OUTPUT\nlow",
        'if/elif/else chooses exactly one path from several conditions. Order matters: the first true branch wins, so put specific checks before broad ones.',
    ),
    'immutability': (
        "# INPUT\nname = 'Mia'\nname = 'Tia'\npoint = (1, 2)\ntry:\n    point[0] = 9\nexcept TypeError as e:\n    print(name)\n    print(type(e).__name__)\n\n# OUTPUT\nTia\nTypeError",
        'Immutable values (str, tuple, int) cannot change in place; you bind a new value instead. Immutability makes data safer to share as dict keys and avoids accidental side effects.',
    ),
    'in': (
        "# INPUT\nallergies = ['penicillin', 'latex']\nprint('latex' in allergies)\nprint('nuts' in allergies)\n\n# OUTPUT\nTrue\nFalse",
        "The in operator tests membership in a collection or substring in text. Use it for allergy checks, allowed codes, or 'needle in haystack' searches.",
    ),
    'int objects': (
        '# INPUT\nn = 42\nprint(n + 1)\nprint(type(n).__name__)\n\n# OUTPUT\n43\nint',
        'Integers are full Python objects (type int), not bare machine slots. They support methods and unlimited size, which is why large counts stay exact.',
    ),
    'is': (
        '# INPUT\na = [1, 2]\nb = [1, 2]\nc = a\nprint(a == b)\nprint(a is b)\nprint(a is c)\n\n# OUTPUT\nTrue\nFalse\nTrue',
        'is checks object identity: same object in memory, not merely equal contents. Use is for None/True/False sentinels; use == for value comparison.',
    ),
    'is None': (
        '# INPUT\nresult = None\nprint(result is None)\nprint(result is not None)\n\n# OUTPUT\nTrue\nFalse',
        "is None is the clear way to test for Python's missing-value marker. Prefer it over == None so identity is explicit and tools stay happy.",
    ),
    'iteration': (
        "# INPUT\nmeds = ['asa', 'metformin']\nfor m in meds:\n    print(m)\n\n# OUTPUT\nasa\nmetformin",
        'Iteration visits items one by one from a collection or stream. for loops, comprehensions, and next() all iterate without you writing index math.',
    ),
    'iteration state': (
        "# INPUT\nit = iter(['a', 'b', 'c'])\nprint(next(it))\nprint(next(it))\nprint(list(it))\n\n# OUTPUT\na\nb\n['c']",
        'Iteration state is the cursor an iterator keeps: which item comes next. After next or a partial for-loop, remaining list(it) only shows what was not yet consumed.',
    ),
}
