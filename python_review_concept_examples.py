"""Complete Review base-concept examples with print + matching OUTPUT."""

CONCEPT_EXAMPLES: dict[str, tuple[str, str]] = {
    '**kwargs': (
        "# INPUT\ndef show_patient(**details):\n    for key, value in details.items():\n        print(key, '->', value)\n\nshow_patient(name='Ana', age=34)\n\n# OUTPUT\nname -> Ana\nage -> 34",
        '**kwargs collects any extra keyword arguments into a dictionary inside the function. It is useful when you do not know in advance which named values the caller will send.',
    ),
    '*args': (
        '# INPUT\ndef total_readings(*readings):\n    return sum(readings)\n\nprint(total_readings(98, 99, 97))\n\n# OUTPUT\n294',
        '*args collects any number of positional arguments into a tuple. It lets one function accept 2 values or 20 values without changing its definition.',
    ),
    '*args/**kwargs': (
        "# INPUT\ndef log_visit(*symptoms, **details):\n    print('symptoms:', symptoms)\n    print('details:', details)\n\nlog_visit('cough', 'fever', doctor='Lee')\n\n# OUTPUT\nsymptoms: ('cough', 'fever')\ndetails: {'doctor': 'Lee'}",
        'Used together, *args gathers extra positional values into a tuple and **kwargs gathers extra named values into a dictionary. This makes a function flexible about what it accepts.',
    ),
    '==': (
        '# INPUT\na = [98, 99]\nb = [98, 99]\nprint(a == b)\nprint(a is b)\n\n# OUTPUT\nTrue\nFalse',
        "The == operator asks 'do these hold equal values?', while is asks 'are these the exact same object in memory?'. Two separate lists with the same contents are == but not is.",
    ),
    'ArrayList': (
        '# INPUT\npatients = []            # like new ArrayList<String>() in Java\npatients.append(\'Ana\')   # like patients.add("Ana")\npatients.append(\'Ben\')\nprint(patients[0])\nprint(len(patients))\n\n# OUTPUT\nAna\n2',
        "A Python list works like Java's ArrayList: a resizable array that grows as you append items and gives fast access by index.",
    ),
    'Big O': (
        "# INPUT\ndef find_name(names, target):\n    steps = 0\n    for name in names:\n        steps += 1\n        if name == target:\n            return steps\n    return steps\n\nnames = ['Ana', 'Ben', 'Cy', 'Dee']\nprint(find_name(names, 'Ana'))\nprint(find_name(names, 'Dee'))\n\n# OUTPUT\n1\n4",
        'Big O describes how the work grows as the input grows. Scanning a list is O(n): in the worst case the number of steps equals the number of items, as the step counts show.',
    ),
    'CRUD': (
        "# INPUT\nrecords = {}\nrecords['p1'] = 'Ana'       # Create\nprint(records['p1'])        # Read\nrecords['p1'] = 'Ana Lee'   # Update\nprint(records['p1'])\ndel records['p1']           # Delete\nprint(len(records))\n\n# OUTPUT\nAna\nAna Lee\n0",
        'CRUD stands for Create, Read, Update, Delete - the four basic operations on stored data. A Python dictionary supports all four directly.',
    ),
    'Decimal': (
        "# INPUT\nfrom decimal import Decimal\n\nprint(0.1 + 0.2)\nprint(Decimal('0.1') + Decimal('0.2'))\n\n# OUTPUT\n0.30000000000000004\n0.3",
        'Decimal (a precise base-10 number type) avoids the tiny rounding errors that regular floats have. Use it for money or medicine doses where exact values matter.',
    ),
    'Enum': (
        '# INPUT\nfrom enum import Enum\n\nclass Status(Enum):\n    ADMITTED = 1\n    DISCHARGED = 2\n\nprint(Status.ADMITTED.name)\nprint(Status.ADMITTED.value)\n\n# OUTPUT\nADMITTED\n1',
        'An Enum gives a fixed set of named choices, like patient statuses, so you cannot accidentally use an invalid value. Each member has a readable name and a value.',
    ),
    'Java streams': (
        '# INPUT\nreadings = [97, 101, 99, 103]\nhigh = [r for r in readings if r > 100]   # like stream().filter(...)\nprint(high)\nprint(sum(high))                          # like a stream reduce/sum\n\n# OUTPUT\n[101, 103]\n204',
        'Java streams chain steps like filter and sum over a collection. Python does the same job with comprehensions and built-ins such as sum(), often in less code.',
    ),
    'KeyError': (
        "# INPUT\nrecords = {'p1': 'Ana'}\ntry:\n    print(records['p2'])\nexcept KeyError as error:\n    print(type(error).__name__)\n\n# OUTPUT\nKeyError",
        'A KeyError happens when you look up a dictionary key that does not exist. Catch it with try/except, or use .get() to receive None instead of an error.',
    ),
    'LEGB': (
        "# INPUT\nname = 'global Ana'\n\ndef clinic():\n    name = 'local Ben'\n    print(name)\n\nclinic()\nprint(name)\n\n# OUTPUT\nlocal Ben\nglobal Ana",
        'LEGB is the order Python searches for a name: Local, Enclosing, Global, Built-in. Inside the function the local name wins; outside, the global one is still untouched.',
    ),
    'None': (
        "# INPUT\ndef find_patient(records, pid):\n    return records.get(pid)   # returns None when missing\n\nresult = find_patient({'p1': 'Ana'}, 'p9')\nprint(result)\nprint(result is None)\n\n# OUTPUT\nNone\nTrue",
        "None is Python's special value meaning 'nothing here'. Functions return it when they have no answer, and you should test for it with 'is None'.",
    ),
    'O(n) shifts': (
        "# INPUT\nqueue = ['Ben', 'Cy', 'Dee']\nshifts = len(queue)      # every existing item moves one slot right\nqueue.insert(0, 'Ana')\nprint(queue)\nprint('items shifted:', shifts)\n\n# OUTPUT\n['Ana', 'Ben', 'Cy', 'Dee']\nitems shifted: 3",
        'Inserting at the front of a list forces every existing item to shift one position, which is O(n) work. For frequent front inserts, a deque is faster.',
    ),
    'Optional': (
        "# INPUT\nfrom typing import Optional\n\ndef find_room(pid) -> Optional[int]:\n    rooms = {'p1': 12}\n    return rooms.get(pid)\n\nprint(find_room('p1'))\nprint(find_room('p9'))\n\n# OUTPUT\n12\nNone",
        "Optional[int] is a type hint meaning 'an int or None'. It warns readers and tools that the function may return no value, so callers should check for None.",
    ),
    'TypeError': (
        "# INPUT\ntry:\n    print('Age: ' + 34)\nexcept TypeError as error:\n    print(type(error).__name__)\n\n# OUTPUT\nTypeError",
        'A TypeError happens when an operation gets the wrong type, like adding text to a number. Convert first (str(34)) or catch the error as shown.',
    ),
    'accumulator': (
        '# INPUT\nreadings = [98, 99, 101]\ntotal = 0\nfor reading in readings:\n    total += reading\nprint(total)\n\n# OUTPUT\n298',
        'An accumulator is a variable that starts empty (often 0) and collects a running result inside a loop. It is the classic way to build totals, counts, or joined text.',
    ),
    'allocation': (
        "# INPUT\ncapacity = 1\nfor items in range(1, 6):\n    if items > capacity:\n        capacity *= 2   # allocate a bigger block, like Python lists do\n    print(items, 'items -> capacity', capacity)\n\n# OUTPUT\n1 items -> capacity 1\n2 items -> capacity 2\n3 items -> capacity 4\n4 items -> capacity 4\n5 items -> capacity 8",
        'Allocation means reserving a block of memory. Lists reserve extra room beyond what they need, so most appends fit without asking for new memory; this simulation shows the capacity growing in jumps.',
    ),
    'amortized complexity': (
        "# INPUT\ncopies = 0\ncapacity = 1\nfor n in range(1, 9):\n    if n > capacity:\n        capacity *= 2\n        copies += n - 1   # copy old items into the new block\nprint('appends:', 8)\nprint('total copies:', copies)\n\n# OUTPUT\nappends: 8\ntotal copies: 7",
        'Amortized complexity averages the cost over many operations. A few appends are expensive (they copy everything), but 8 appends needed only 7 copies total, so the average cost per append stays small - amortized O(1).',
    ),
    'and/or': (
        "# INPUT\npulse = 72\nprint(pulse > 60 and pulse < 100)\nname = '' or 'Unknown'\nprint(name)\n\n# OUTPUT\nTrue\nUnknown",
        'and is True only when both sides are True; or returns the first truthy value it finds. The or trick is a common way to supply a default when a value is empty.',
    ),
    'arithmetic operators': (
        '# INPUT\nprint(7 + 3)\nprint(7 / 2)    # true division gives a float\nprint(7 // 2)   # floor division drops the fraction\nprint(7 % 2)    # remainder\nprint(2 ** 3)   # power\n\n# OUTPUT\n10\n3.5\n3\n1\n8',
        "Python's arithmetic operators cover addition, two kinds of division, remainder, and powers. Note that / always gives a float while // keeps whole numbers.",
    ),
    'assignment expressions': (
        "# INPUT\nreadings = [98, 104, 99]\nif (highest := max(readings)) > 100:\n    print('alert:', highest)\n\n# OUTPUT\nalert: 104",
        'The walrus operator := assigns a value and uses it in the same expression. Here it saves computing max(readings) twice: once for the test and once for printing.',
    ),
    'associativity': (
        '# INPUT\nprint(2 ** 3 ** 2)     # ** groups right to left: 2 ** 9\nprint((2 ** 3) ** 2)   # forced left first: 8 ** 2\nprint(10 - 4 - 3)      # - groups left to right: (10 - 4) - 3\n\n# OUTPUT\n512\n64\n3',
        'Associativity decides grouping when the same operator repeats. Most operators group left to right, but ** groups right to left, which changes the answer a lot.',
    ),
    'authorization': (
        "# INPUT\ndef can_view_records(role):\n    return role in ('doctor', 'nurse')\n\nprint(can_view_records('doctor'))\nprint(can_view_records('visitor'))\n\n# OUTPUT\nTrue\nFalse",
        'Authorization checks what an already-identified user is allowed to do. Here only doctors and nurses may view patient records; visitors are denied.',
    ),
    'average O(1)': (
        "# INPUT\nsmall = {'p1': 'Ana'}\nbig = {f'p{i}': 'x' for i in range(10000)}\nprint(small['p1'])\nprint(big['p9999'])   # just as fast: one hash, one slot\n\n# OUTPUT\nAna\nx",
        'Dictionary lookup is O(1) on average: it hashes the key and jumps straight to its slot, so finding a key in 10,000 entries costs about the same as in 1.',
    ),
    'base case': (
        "# INPUT\ndef countdown(n):\n    if n == 0:          # base case stops the recursion\n        print('done')\n        return\n    print(n)\n    countdown(n - 1)\n\ncountdown(3)\n\n# OUTPUT\n3\n2\n1\ndone",
        'The base case is the condition where a recursive function stops calling itself. Without it the function would recurse forever and crash the call stack.',
    ),
    'bitwise AND': (
        '# INPUT\nprint(12 & 10)        # 1100 & 1010 = 1000\nprint(bin(12 & 10))\n\n# OUTPUT\n8\n0b1000',
        'Bitwise AND (&) keeps a 1 only where both numbers have a 1 in the same bit position. It is often used to test whether specific flag bits are set.',
    ),
    'bitwise NOT': (
        '# INPUT\nprint(~5)    # flips every bit: ~n equals -n - 1\nprint(~0)\n\n# OUTPUT\n-6\n-1',
        'Bitwise NOT (~) flips every bit of a number. Because Python integers are signed, the result follows the rule ~n == -n - 1, so ~5 is -6.',
    ),
    'bitwise OR': (
        '# INPUT\nprint(12 | 10)        # 1100 | 1010 = 1110\nprint(bin(12 | 10))\n\n# OUTPUT\n14\n0b1110',
        'Bitwise OR (|) sets a 1 where either number has a 1 in that bit position. It is commonly used to combine several flag bits into one value.',
    ),
    'bool branching': (
        "# INPUT\npatients = []\nif patients:\n    print('list has items')\nelse:\n    print('list is empty')\nname = 'Ana'\nif name:\n    print('name is set')\n\n# OUTPUT\nlist is empty\nname is set",
        "Python treats empty things ([], '', 0, None) as False and non-empty things as True, so you can branch directly on a value without writing == or len().",
    ),
    'break': (
        "# INPUT\nfor reading in [98, 99, 104, 97]:\n    if reading > 100:\n        print('alert at', reading)\n        break\n    print('ok', reading)\n\n# OUTPUT\nok 98\nok 99\nalert at 104",
        'break exits the loop immediately, skipping all remaining items. Use it when you have found what you were looking for, like the first alarming reading.',
    ),
    'call stack': (
        "# INPUT\ndef check_vitals():\n    print('checking vitals')\n\ndef see_patient():\n    print('start visit')\n    check_vitals()\n    print('end visit')\n\nsee_patient()\n\n# OUTPUT\nstart visit\nchecking vitals\nend visit",
        'The call stack tracks which function is running and where to return afterwards. see_patient pauses while check_vitals runs on top of it, then resumes exactly where it left off.',
    ),
    'case folding': (
        "# INPUT\ntyped = 'ANA@CLINIC.COM'\nstored = 'ana@clinic.com'\nprint(typed.casefold())\nprint(typed.casefold() == stored.casefold())\n\n# OUTPUT\nana@clinic.com\nTrue",
        "Case folding converts text to a standard lowercase form made for comparing, so 'ANA' and 'ana' match. It is stronger than lower() for some international characters.",
    ),
    'circular references': (
        '# INPUT\nclass Patient:\n    pass\n\na = Patient()\nb = Patient()\na.buddy = b\nb.buddy = a   # each object points at the other: a cycle\nprint(a.buddy is b)\nprint(b.buddy is a)\n\n# OUTPUT\nTrue\nTrue',
        'A circular reference is when objects point at each other in a loop. Reference counting alone cannot free such objects, which is why Python also runs a cycle-detecting garbage collector.',
    ),
    'class design': (
        "# INPUT\nclass Patient:\n    def __init__(self, name, pulse):\n        self.name = name\n        self.pulse = pulse\n\n    def is_healthy(self):\n        return 60 <= self.pulse <= 100\n\np = Patient('Ana', 72)\nprint(p.name)\nprint(p.is_healthy())\n\n# OUTPUT\nAna\nTrue",
        'Good class design bundles related data (name, pulse) with the behavior that uses it (is_healthy). Callers work with one clear object instead of loose variables.',
    ),
    'closures': (
        '# INPUT\ndef make_counter():\n    count = 0\n    def next_visit():\n        nonlocal count\n        count += 1\n        return count\n    return next_visit\n\ncounter = make_counter()\nprint(counter())\nprint(counter())\n\n# OUTPUT\n1\n2',
        'A closure is an inner function that remembers variables from the function that created it, even after that outer function has finished. Here each call still sees and updates count.',
    ),
    'collisions': (
        "# INPUT\nbuckets = 8\nprint(hash(1) % buckets)\nprint(hash(9) % buckets)   # same slot -> a collision\nd = {1: 'Ana', 9: 'Ben'}\nprint(d[9])                # dict resolves it, lookup still correct\n\n# OUTPUT\n1\n1\nBen",
        "A collision happens when two different keys hash to the same slot in a dictionary's table. Python quietly probes for another slot, so lookups still return the right value.",
    ),
    'comma operator': (
        '# INPUT\npoint = 3, 4       # commas build a tuple (Python has no C-style comma operator)\nprint(point)\na, b = 1, 2\na, b = b, a        # swap using tuple packing and unpacking\nprint(a, b)\n\n# OUTPUT\n(3, 4)\n2 1',
        "In Python a comma does not discard values like C's comma operator; it builds a tuple. That is what makes the one-line swap a, b = b, a work.",
    ),
    'comparison operators': (
        '# INPUT\npulse = 72\nprint(pulse > 60)\nprint(pulse == 72)\nprint(pulse != 100)\nprint(60 <= pulse <= 100)   # chained comparison\n\n# OUTPUT\nTrue\nTrue\nTrue\nTrue',
        'Comparison operators (>, <, ==, !=, >=, <=) return True or False. Python also allows chaining, so 60 <= pulse <= 100 reads like the math it represents.',
    ),
    'comprehensions': (
        "# INPUT\nreadings = [97, 101, 99, 103]\nfevers = [r for r in readings if r > 100]\nlabels = {r: 'high' for r in fevers}\nprint(fevers)\nprint(labels)\n\n# OUTPUT\n[101, 103]\n{101: 'high', 103: 'high'}",
        'A comprehension builds a new list, dict, or set in one readable line: take each item, optionally filter it, and transform it. It replaces a multi-line loop with append.',
    ),
    'conditionals': (
        "# INPUT\ntemp = 101\nif temp > 103:\n    print('emergency')\nelif temp > 100:\n    print('fever')\nelse:\n    print('normal')\n\n# OUTPUT\nfever",
        'Conditionals choose one path of code based on a test. Python checks if, then each elif in order, and runs else only when nothing above matched.',
    ),
    'copying': (
        '# INPUT\noriginal = [98, 99]\nalias = original          # same list, second name\nclone = original.copy()   # a separate new list\noriginal.append(104)\nprint(alias)\nprint(clone)\n\n# OUTPUT\n[98, 99, 104]\n[98, 99]',
        'Assignment only creates another name for the same list, so changes show through both names. Use .copy() when you need an independent list that will not change with the original.',
    ),
    'cyclic GC': (
        '# INPUT\nimport gc\nimport weakref\n\nclass Node:\n    pass\n\na = Node()\na.self_ref = a            # a reference cycle\nwatcher = weakref.ref(a)\ndel a                     # refcount alone cannot free the cycle\ngc.collect()              # the cyclic garbage collector can\nprint(watcher() is None)\n\n# OUTPUT\nTrue',
        "Python's cyclic garbage collector finds groups of objects that only reference each other and frees them. The weak reference turning to None proves the cycle was reclaimed.",
    ),
    'dataclass': (
        "# INPUT\nfrom dataclasses import dataclass\n\n@dataclass\nclass Patient:\n    name: str\n    pulse: int\n\np = Patient('Ana', 72)\nprint(p)\nprint(p.pulse)\n\n# OUTPUT\nPatient(name='Ana', pulse=72)\n72",
        '@dataclass writes __init__, __repr__, and comparison methods for you from the field list. It is the quickest way to make a small class that mainly holds data.',
    ),
    'default values': (
        "# INPUT\ndef greet(name, ward='General'):\n    print(name, '-', ward)\n\ngreet('Ana')\ngreet('Ben', 'ICU')\n\n# OUTPUT\nAna - General\nBen - ICU",
        'A default value is used when the caller leaves that argument out, making the parameter optional. Avoid mutable defaults like []; prefer None and create the list inside.',
    ),
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
        '# INPUT\n'
        'def is_even(n):\n'
        '    return n % 2 == 0\n'
        '\n'
        'nums = [1, 2, 3, 4, 5]\n'
        'evens = list(filter(is_even, nums))\n'
        'print(evens)\n'
        '\n'
        '# OUTPUT\n'
        '[2, 4]',
        'filter keeps only items that pass your test function. True means keep; False means skip.',
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


def lookup_concept(name: str) -> tuple[str, str]:
    """Return (example_with_input_output, explanation); fallback if unknown."""
    if name in CONCEPT_EXAMPLES:
        return CONCEPT_EXAMPLES[name]
    return (
        f"# INPUT\nprint({name!r})\n\n# OUTPUT\n{name}",
        f"Core idea for this question: {name}.",
    )
