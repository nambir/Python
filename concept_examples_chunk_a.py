"""Self-contained Review base-concept examples."""

CHUNK = {
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
}
