"""Self-contained Review base-concept examples."""

CHUNK = {
    'rounding policy': (
        "# INPUT\nfrom decimal import Decimal, ROUND_HALF_UP\ndose = Decimal('2.345')\nrounded = dose.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)\nprint(rounded)\n\n# OUTPUT\n2.35",
        'A rounding policy is a fixed rule for cutting or raising decimals (what + how). Use it for money or drug doses so every run rounds the same way.',
    ),
    'rule precedence': (
        '# INPUT\nready = True\npaid = False\nprint(not ready and paid)\nprint(not (ready and paid))\n\n# OUTPUT\nFalse\nTrue',
        'Rule precedence decides which part of a combined check runs first. `not` binds tighter than `and`, so add parentheses when you mean a different grouping.',
    ),
    'runtime data': (
        '# INPUT\n# value arrives while the program runs (sensor, form, API)\nheart_rate = 72\nprint(heart_rate)\n\n# OUTPUT\n72',
        'Runtime data is information known only after the program starts. Use it for live readings (heart rate, form answers) instead of hard-coding every value.',
    ),
    'runtime validation': (
        "# INPUT\nage = -3\ntry:\n    if age < 0:\n        raise ValueError('age must be >= 0')\nexcept ValueError as e:\n    print(type(e).__name__ + ': ' + str(e))\n\n# OUTPUT\nValueError: age must be >= 0",
        'Runtime validation checks real values while the program runs. Use it to reject bad patient ages or doses before they cause wrong results.',
    ),
    'scalar values': (
        "# INPUT\nage = 10\nunit = 'mg'\nprint(age)\nprint(unit)\n\n# OUTPUT\n10\nmg",
        'A scalar is one simple value (number, string, bool), not a whole list or dict. Use scalars for single facts like age or a unit label.',
    ),
    'search': (
        "# INPUT\ncodes = ['A01', 'B12', 'C03']\nprint('B12' in codes)\n\n# OUTPUT\nTrue",
        'Search looks for a wanted item inside a collection. Use `in` for a clear yes/no check, such as finding a diagnosis code.',
    ),
    'set comprehension': (
        '# INPUT\ntemps = [98.6, 99.1, 98.6, 100.0]\nhigh = {t for t in temps if t >= 99.0}\nprint(sorted(high))\n\n# OUTPUT\n[99.1, 100.0]',
        'A set comprehension builds a set with a compact loop. Use it when you want unique values that pass a filter (here: unique high temps).',
    ),
    'set intersection': (
        "# INPUT\nmorning = {'A01', 'B12'}\nevening = {'B12', 'C03'}\nprint(sorted(morning & evening))\n\n# OUTPUT\n['B12']",
        'Set intersection keeps only items that appear in both sets. Use it to find shared allergy codes or overlapping clinic IDs.',
    ),
    'set membership': (
        "# INPUT\nseen = {'Mia', 'Sam'}\nprint('Mia' in seen)\n\n# OUTPUT\nTrue",
        'Set membership checks whether a value is in a set. Use sets when you need a fast yes/no for IDs already processed.',
    ),
    'setdefault': (
        "# INPUT\ncounts = {}\ncounts.setdefault('fever', 0)\ncounts['fever'] += 1\nprint(counts)\n\n# OUTPUT\n{'fever': 1}",
        "`setdefault` returns a key's value, or creates the key with a default if missing. Use it when tallying symptoms so the first sighting starts at 0 safely.",
    ),
    'shadowing': (
        "# INPUT\nunit = 'mg'\ndef dose():\n    unit = 'ml'  # shadows the outer name inside this function\n    print(unit)\ndose()\nprint(unit)\n\n# OUTPUT\nml\nmg",
        'Shadowing means a nearby name hides an outer name with the same spelling. Avoid shadowing builtins like `len`, and know that the inner name does not change the outer one.',
    ),
    'short-circuiting': (
        "# INPUT\ndef check():\n    print('checked')\n    return True\nprint(False and check())\nprint(True or check())\n\n# OUTPUT\nFalse\nTrue",
        'Short-circuiting stops an `and`/`or` check as soon as the answer is known. Use it to skip extra work (or avoid errors) when the left side already decides the result.',
    ),
    'sorted': (
        "# INPUT\nnames = ['Sam', 'Mia', 'Alex']\nprint(sorted(names))\nprint(names)\n\n# OUTPUT\n['Alex', 'Mia', 'Sam']\n['Sam', 'Mia', 'Alex']",
        '`sorted` returns a new ordered list and leaves the original alone. Use it when you need patients or labels in order without mutating the source list.',
    ),
    'sorted key': (
        "# INPUT\nwords = ['fever', 'flu', 'cold']\nprint(sorted(words, key=len))\n\n# OUTPUT\n['flu', 'cold', 'fever']",
        '`key=` tells `sorted` what to compare for each item. Use it to sort by length, temperature field, or any derived value.',
    ),
    'static scope': (
        "# INPUT\nlabel = 'clinic'\ndef show():\n    print(label)  # resolves using where the code is written\nshow()\n\n# OUTPUT\nclinic",
        'Static scope means Python finds names based on where the code is written, not who called it. A nested function looks outward to enclosing and global names in that written structure.',
    ),
    'static typing': (
        '# INPUT\nage: int = 42  # hint for readers/tools; runtime still stores a normal int\nprint(age)\nprint(type(age).__name__)\n\n# OUTPUT\n42\nint',
        'Static typing uses type information to catch mistakes before (or without) relying on a crash. In Python, hints help tools like mypy; they do not enforce types by themselves at runtime.',
    ),
    'str objects': (
        "# INPUT\nnote = 'rest'\nprint(type(note).__name__)\nprint(note.upper())\n\n# OUTPUT\nstr\nREST",
        '`str` objects hold text and provide text methods. Use them for names, notes, and codes; call methods like `upper()` when you need a new string.',
    ),
    'string equality': (
        "# INPUT\nstatus = 'ok'\nprint(status == 'ok')\nprint(status == 'OK')\n\n# OUTPUT\nTrue\nFalse",
        'String equality (`==`) compares the characters inside two strings. Use it for text checks; case matters unless you normalize first.',
    ),
    'string growth / UTF-16': (
        "# INPUT\ntext = 'fever'\nbefore_id = id(text)\ntext += '!'\nprint(text)\nprint(before_id != id(text))\n\n# OUTPUT\nfever!\nTrue",
        'Python strings are immutable, so growing with `+=` builds a new string object. That differs from C# details around UTF-16 buffers/StringBuilder; prefer lists/join for heavy growth.',
    ),
    'string interning': (
        "# INPUT\na = 'patient'\nb = 'patient'\nprint(a == b)  # compare text with ==\n# do not rely on (a is b); identity may vary by implementation\n\n# OUTPUT\nTrue",
        'Interning may reuse some identical string objects, but that is not a guarantee. Always compare text with `==`; treat `is` as identity and implementation-dependent here.',
    ),
    'subscription': (
        "# INPUT\nvitals = {'hr': 72, 'temp': 98.6}\ntemps = [98.6, 99.1]\nprint(vitals['hr'])\nprint(temps[0])\n\n# OUTPUT\n72\n98.6",
        'Subscription means using `[]` to get an item by key or index. Use it to read one vital from a dict or one temperature from a list.',
    ),
    'sum': (
        '# INPUT\ndoses_mg = [10, 20, 15]\nprint(sum(doses_mg))\n\n# OUTPUT\n45',
        '`sum` adds all numbers in an iterable. Use it for totals such as daily dose milligrams.',
    ),
    'sys.getsizeof': (
        '# INPUT\nimport sys\nprint(sys.getsizeof([]) > sys.getsizeof(()))\n\n# OUTPUT\nTrue',
        "`sys.getsizeof` reports an object's shallow size in bytes, but exact numbers vary by Python build. Compare relationships (list empty shell vs empty tuple) instead of memorizing a fixed byte count.",
    ),
    'trailing comma': (
        '# INPUT\ngrouped = (98.6)\none_item = (98.6,)\nprint(type(grouped).__name__)\nprint(type(one_item).__name__)\nprint(one_item[0])\n\n# OUTPUT\nfloat\ntuple\n98.6',
        'A trailing comma makes a one-item tuple; parentheses alone only group. Use `(98.6,)` when an API expects a sequence of readings, not a bare float.',
    ),
    'truthy tests': (
        "# INPUT\nalerts = []\nprint(bool(alerts))\nif not alerts:\n    print('no alerts')\n\n# OUTPUT\nFalse\nno alerts",
        "Truthy tests ask whether a value acts like true or false in an `if`. Empty lists/dicts/strings are falsey - handy for 'any alerts?' checks.",
    ),
    'tuple': (
        '# INPUT\npoint = (3, 4)\nprint(point)\nprint(point[0])\n\n# OUTPUT\n(3, 4)\n3',
        'A tuple is an ordered collection that you do not change in place. Use it for fixed records such as coordinates or a vital-sign snapshot.',
    ),
    'tuple immutability': (
        "# INPUT\nreading = (120, 80)\ntry:\n    reading[0] = 130\nexcept TypeError as e:\n    print(type(e).__name__ + ': ' + str(e))\n\n# OUTPUT\nTypeError: 'tuple' object does not support item assignment",
        'Tuple immutability means you cannot replace an item after creation. Make a new tuple when a blood-pressure pair must change.',
    ),
    'tuple literal': (
        '# INPUT\npoint = 3, 4\nprint(point)\nprint(type(point).__name__)\n\n# OUTPUT\n(3, 4)\ntuple',
        'A tuple literal is written with commas (parentheses are optional for multi-item tuples). The comma is what builds the tuple, not the parentheses alone.',
    ),
    'tuple unpacking': (
        "# INPUT\nreading = (120, 80, 98.6, '2024-01-15')\nsys_bp, dia_bp, temp, date = reading\nprint(sys_bp)\nprint(dia_bp)\nprint(temp)\nprint(date)\n\n# OUTPUT\n120\n80\n98.6\n2024-01-15",
        'Tuple unpacking pulls each field into its own name in one step. Use it for a patient reading so each vital is clear without repeated indexing.',
    ),
    'type annotations': (
        "# INPUT\npatient_id: str = 'P100'\nprint(patient_id)\n\n# OUTPUT\nP100",
        'Type annotations label the expected type of a name. They document intent for readers and checkers; Python still runs the assignment normally.',
    ),
    'type hints': (
        '# INPUT\ndef to_celsius(f: float) -> float:\n    return (f - 32) * 5 / 9\nprint(round(to_celsius(98.6), 1))\n\n# OUTPUT\n37.0',
        'Type hints mark parameter and return types on functions. Use them so tools and teammates know a converter expects floats and returns a float.',
    ),
    'type inspection': (
        '# INPUT\ntemp = 98.6\nprint(isinstance(temp, float))\nprint(type(temp).__name__)\n\n# OUTPUT\nTrue\nfloat',
        'Type inspection asks what kind of object a value is at runtime. Use `isinstance` when behavior must branch on the actual type.',
    ),
    'unlimited Python int': (
        '# INPUT\nhuge = 10 ** 50\nprint(huge)\nprint(type(huge).__name__)\n\n# OUTPUT\n100000000000000000000000000000000000000000000000000\nint',
        'Python `int` values grow as large as memory allows (not a fixed 32/64-bit box). Use them when counts or powers would overflow a fixed-size integer type elsewhere.',
    ),
    'visited set': (
        "# INPUT\nvisited = set()\npath = ['A', 'B', 'A', 'C']\nfor node in path:\n    if node in visited:\n        print('skip ' + node)\n    else:\n        visited.add(node)\n        print('visit ' + node)\n\n# OUTPUT\nvisit A\nvisit B\nskip A\nvisit C",
        'A visited set remembers nodes already checked. Use it in graph/search walks so you do not process the same room or ID twice.',
    ),
    'walrus operator': (
        '# INPUT\ntemps = [98.6, 99.1, 97.0]\nif (n := len(temps)) > 2:\n    print(n)\n\n# OUTPUT\n3',
        'The walrus operator `:=` assigns a name and uses that value in the same expression. Use it to avoid calling `len` twice when the count is both tested and printed.',
    ),
    'weakref': (
        '# INPUT\nimport weakref\nclass Patient:\n    pass\np = Patient()\nref = weakref.ref(p)\nprint(ref() is p)\n\n# OUTPUT\nTrue',
        'A weakref points at an object without keeping it alive by itself. Use it for caches that should not stop garbage collection of unused patients/objects.',
    ),
    'while loops': (
        '# INPUT\ncount = 0\nwhile count < 3:\n    count += 1\nprint(count)\n\n# OUTPUT\n3',
        'A `while` loop repeats as long as a condition stays true. Use it when you do not know the count up front, or you wait until a counter/flag changes.',
    ),
    'yield': (
        '# INPUT\ndef temps():\n    yield 98.6\n    yield 99.1\nprint(list(temps()))\n\n# OUTPUT\n[98.6, 99.1]',
        '`yield` pauses a generator and sends out one value at a time. Use it for large reading streams so you do not build the whole list in memory first.',
    ),
    'zip': (
        "# INPUT\nnames = ['Mia', 'Sam']\nscores = [90, 85]\nprint(list(zip(names, scores)))\nreadings = [\n    (120, 80, 98.6),\n    (115, 75, 99.1),\n]\nprint(list(zip(*readings)))\n\n# OUTPUT\n[('Mia', 90), ('Sam', 85)]\n[(120, 115), (80, 75), (98.6, 99.1)]",
        '`zip` pairs items from iterables by position. `zip(names, scores)` builds rows of pairs; `zip(*readings)` turns row tuples into column tuples.',
    ),
}
