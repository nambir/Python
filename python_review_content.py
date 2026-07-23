"""Healthcare-themed Python review question bank."""
DOCX_NAME = 'python-practice-questions-2025-26.docx'
DOCX_TITLE = 'Python Practice Questions - 2025'
DOCX_LEVEL = 'Python - Senior Developer Level'
QUESTIONS: list[dict] = [{'id': 'Q1.1',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'coding',
  'title': 'Patient bill calculation',
  'question': "You're working on a patient billing system. Write a function that calculates the "
              "total cost for a patient's hospital stay, handling different data types "
              'appropriately.',
  'answer': 'Validate that monetary inputs and days are non-negative; calculate subtotal once, '
            'derive the conditional discount, and return named fields. Real billing code should '
            'use Decimal and an explicit rounding policy rather than binary float.',
  'learn_intent': 'Practice monetary calculations without mixing business rules and presentation.',
  'base_concepts': ['function parameters',
                    'bool branching',
                    'Decimal',
                    'rounding policy',
                    'dictionary return values'],
  'topic_deepdive': '<p>Money should not be represented by binary float at a billing boundary '
                    'because values such as 0.1 cannot be represented exactly.</p><p>Use Decimal, '
                    'define when rounding occurs, and keep subtotal, discount, and final amount as '
                    'separate auditable values.</p>',
  'interview_qa': [{'q': 'Why is Decimal preferable here?',
                    'a': 'It preserves decimal arithmetic and lets the system state a rounding '
                         'policy.'},
                   {'q': 'When is the insurance discount applied?',
                    'a': 'After calculating the stay subtotal, before final currency rounding.'}],
  'code_file': 'Q1_1_patient_bill.py',
  'subsection': 'Primitive Datatypes',
  'prompt_full': "You're working on a patient billing system. Write a function that calculates the "
                 "total cost for a patient's hospital stay, handling different data types "
                 'appropriately.',
  'code_stub': 'def calculate_patient_bill(room_charge_per_day: float, days_stayed: int, \n'
               '                          has_insurance: bool, patient_name: str) -> dict:\n'
               '    """\n'
               '    Calculate total bill for a patient\n'
               '    - Apply 20% discount if patient has insurance\n'
               '    - Return a dictionary with patient details and final amount\n'
               '    """\n'
               '    # Your implementation here\n'
               '    pass',
  'expected_output': 'Expected Output: Handle type conversions, boolean logic, and string '
                     'formatting.'},
 {'id': 'Q1.2',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'reasoning',
  'title': 'Integer or string patient IDs',
  'question': 'In a healthcare database, patient IDs are sometimes stored as integers (12345) and '
              'sometimes as strings ("P12345"). Explain the memory allocation differences between '
              'these two approaches and when you would use each in a hospital management system.',
  'answer': 'An int has a compact numeric payload while a string owns character storage plus '
            'object metadata, so a numeric key is normally cheaper. Use an internal numeric '
            'database key for joins and a prefixed, opaque string identifier at public boundaries; '
            'never rely on either representation as authorization.',
  'learn_intent': 'Distinguish an internal database identity from an externally visible patient '
                  'identifier.',
  'base_concepts': ['int objects',
                    'str objects',
                    'object memory',
                    'primary keys',
                    'opaque identifiers'],
  'topic_deepdive': '<p>Integers store numeric values compactly; strings also need character '
                    'storage and metadata.</p><p>A public identifier such as P12345 can be '
                    'meaningful to humans, but it must not become an authorization secret.</p>',
  'interview_qa': [{'q': 'Should a public patient ID be a database primary key?',
                    'a': 'Usually no; an internal surrogate key decouples storage from public '
                         'formatting.'},
                   {'q': 'Does a string ID make data secure?',
                    'a': 'No. Access control must be enforced independently.'}],
  'subsection': 'Primitive Datatypes',
  'prompt_full': 'In a healthcare database, patient IDs are sometimes stored as integers (12345) '
                 'and sometimes as strings ("P12345"). Explain the memory allocation differences '
                 'between these two approaches and when you would use each in a hospital '
                 'management system.',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q1.3',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'coding',
  'title': 'Medication schedule',
  'question': "You're managing a patient's medication schedule. Create a system to track daily "
              'medications:',
  'answer': 'Use dict[str, list[str]] with setdefault for grouping. Encapsulate mutation, remove '
            'empty buckets, and return copies from lookup so callers cannot mutate schedule state '
            'unexpectedly.',
  'learn_intent': 'Model one-to-many schedule data and avoid leaking mutable internal lists.',
  'base_concepts': ['dict', 'list', 'setdefault', 'mutation', 'defensive copying'],
  'topic_deepdive': '<p>A time is the lookup key and several medications can share it, making '
                    'dict[str, list[str]] a natural model.</p><p>Returning a copy from a lookup '
                    'stops a caller from accidentally changing the stored schedule.</p>',
  'interview_qa': [{'q': 'Why not use a single medication per time?',
                    'a': 'Multiple prescriptions can be due at the same time.'},
                   {'q': 'What should happen after removing the final medication?',
                    'a': 'Delete the empty time bucket to keep the representation clean.'}],
  'code_file': 'Q1_3_medication_schedule.py',
  'subsection': 'List Operations',
  'prompt_full': "You're managing a patient's medication schedule. Create a system to track daily "
                 'medications:',
  'code_stub': 'def manage_medication_schedule(patient_medications: list) -> dict:\n'
               '    """\n'
               '    Given a list of medications with their schedules:\n'
               "    [('Aspirin', '8:00'), ('Insulin', '8:00'), ('Aspirin', '20:00')]\n"
               '    \n'
               '    Return a dictionary grouped by time:\n'
               "    {'8:00': ['Aspirin', 'Insulin'], '20:00': ['Aspirin']}\n"
               '    \n'
               '    Also implement methods to:\n'
               '    1. Add new medication\n'
               '    2. Remove medication at specific time\n'
               '    3. Get all medications for a specific time\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q1.4',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'reasoning',
  'title': 'List insertion costs',
  'question': 'What is the underlying data structure of Python lists? How does this affect '
              "performance when you're inserting patient records at the beginning vs. end of a "
              "large patient queue? Compare with Java's ArrayList.",
  'answer': 'Lists are over-allocated contiguous arrays of object references. append is amortized '
            'O(1), whereas insert(0, value) shifts n references and is O(n); Java ArrayList has '
            'the same broad behavior. Use collections.deque for FIFO triage queues.',
  'learn_intent': 'Choose a queue structure by operation cost rather than by familiarity.',
  'base_concepts': ['dynamic arrays', 'amortized complexity', 'O(n) shifts', 'deque', 'ArrayList'],
  'topic_deepdive': '<p>Python lists are dynamic arrays of references. Appending is amortized '
                    'O(1), but a front insert shifts every existing reference.</p><p>Java '
                    'ArrayList has the same broad cost profile; a deque is the better FIFO triage '
                    'queue.</p>',
  'interview_qa': [{'q': 'Why is append only amortized O(1)?',
                    'a': 'Occasional resize copies are expensive, but spread across many cheap '
                         'appends.'},
                   {'q': 'Which operation makes list a poor queue?',
                    'a': 'Repeated pop(0) or insert(0, item).'}],
  'subsection': 'List Operations',
  'prompt_full': 'What is the underlying data structure of Python lists? How does this affect '
                 "performance when you're inserting patient records at the beginning vs. end of a "
                 "large patient queue? Compare with Java's ArrayList.",
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q1.5',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'coding',
  'title': 'Immutable vital-sign statistics',
  'question': 'Design a system to store immutable patient vital signs readings:',
  'answer': 'Reject an empty collection, unpack readings, and compute aggregates from the '
            'appropriate columns. Return a tuple for a stable report snapshot and make date-range '
            'ordering explicit.',
  'learn_intent': 'Aggregate structured immutable readings while handling the empty-input edge '
                  'case.',
  'base_concepts': ['tuple unpacking', 'zip', 'sum', 'max', 'empty collections'],
  'topic_deepdive': '<p>Each reading has a fixed positional schema, so tuple unpacking makes the '
                    'aggregation explicit.</p><p>An empty series has no average or maximum; fail '
                    'clearly rather than inventing a clinical value.</p>',
  'interview_qa': [{'q': 'Why return a tuple report?',
                    'a': 'It communicates a fixed, immutable result shape.'},
                   {'q': 'How should dates be compared?',
                    'a': 'Use parsed date objects in real systems, not arbitrary display '
                         'strings.'}],
  'code_file': 'Q1_5_vital_signs.py',
  'subsection': 'Tuple Operations',
  'prompt_full': 'Design a system to store immutable patient vital signs readings:',
  'code_stub': 'def process_vital_signs(readings: list) -> tuple:\n'
               '    """\n'
               '    Process vital signs readings and return statistics\n'
               "    Input: [(120, 80, 98.6, '2024-01-15'), (115, 75, 99.1, '2024-01-16')]\n"
               '    Output: Tuple of (avg_systolic, avg_diastolic, max_temp, date_range)\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q1.6',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'reasoning',
  'title': 'Single-item tuple syntax',
  'question': 'Why does temp_reading = (98.6) create a float instead of a tuple, but temp_reading '
              '= (98.6,) creates a tuple? How does this relate to storing single vital sign '
              'measurements in healthcare applications?',
  'answer': 'Parentheses group expressions; the comma constructs a tuple. Store a scalar reading '
            'as a float unless the API deliberately requires a one-item immutable sequence, in '
            'which case write (98.6,).',
  'learn_intent': 'Learn that the comma, not parentheses, creates a tuple.',
  'base_concepts': ['expression grouping', 'tuple literal', 'trailing comma', 'scalar values'],
  'topic_deepdive': '<p>Parentheses merely group 98.6, so its type remains float. A comma creates '
                    'the one-item tuple.</p><p>This matters when an API expects a sequence of '
                    'readings rather than one scalar measurement.</p>',
  'interview_qa': [{'q': 'What is type((98.6,))?', 'a': 'tuple.'},
                   {'q': 'Can parentheses alone create an empty tuple?',
                    'a': 'No; () is a special empty tuple literal.'}],
  'subsection': 'Tuple Operations',
  'prompt_full': 'Why does temp_reading = (98.6) create a float instead of a tuple, but '
                 'temp_reading = (98.6,) creates a tuple? How does this relate to storing single '
                 'vital sign measurements in healthcare applications?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q1.7',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'reasoning',
  'title': 'Tuples versus lists for coordinates',
  'question': 'Compare the memory footprint and access speed of tuples vs lists when storing '
              'thousands of patient coordinate data (x, y, z) for medical imaging. Why would you '
              'choose one over the other?',
  'answer': 'Tuples avoid list over-allocation and are immutable, so they are smaller and often '
            'slightly faster to iterate. Choose tuples for fixed coordinates and lists only when '
            'the collection or coordinate values must be edited.',
  'learn_intent': 'Select immutable tuples or mutable lists based on coordinate lifecycle.',
  'base_concepts': ['immutability', 'memory overhead', 'iteration', 'hashability', 'mutation'],
  'topic_deepdive': '<p>Tuples have a fixed size and no spare capacity, so they typically need '
                    'less memory than lists.</p><p>Use tuples for captured imaging coordinates and '
                    'lists when a working algorithm must edit or append points.</p>',
  'interview_qa': [{'q': 'Can a coordinate tuple be a dict key?',
                    'a': 'Yes, if every coordinate component is hashable.'},
                   {'q': 'Why are lists larger?',
                    'a': 'They retain mutable-container state and over-allocation capacity.'}],
  'subsection': 'Tuple Operations',
  'prompt_full': 'Compare the memory footprint and access speed of tuples vs lists when storing '
                 'thousands of patient coordinate data (x, y, z) for medical imaging. Why would '
                 'you choose one over the other?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q1.8',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'coding',
  'title': 'Nested patient records',
  'question': 'Create a patient record management system using dictionaries:',
  'answer': 'Use a mapping keyed by patient ID and validate required nested fields at the '
            'boundary. Copy incoming mutable structures where ownership matters, search with '
            'normalized blood types, and avoid exposing mutable internal visits directly.',
  'learn_intent': 'Design nested records without exposing accidental shared mutation.',
  'base_concepts': ['nested dictionaries', 'CRUD', 'copying', 'normalization', 'search'],
  'topic_deepdive': '<p>Nested dictionaries are useful for a small in-memory model, but their '
                    'schema must be consistently validated.</p><p>Copy incoming mutable values and '
                    'return copies of visit histories so callers cannot mutate stored records '
                    'invisibly.</p>',
  'interview_qa': [{'q': 'When should this become database tables?',
                    'a': 'When querying, concurrency, relationships, or audit requirements grow.'},
                   {'q': 'Why normalize blood types?',
                    'a': 'Case and whitespace differences otherwise make searches unreliable.'}],
  'code_file': 'Q1_8_patient_records.py',
  'subsection': 'Dictionary Operations',
  'prompt_full': 'Create a patient record management system using dictionaries:',
  'code_stub': 'def patient_record_system():\n'
               '    """\n'
               '    Create a system that manages patient records with nested dictionaries:\n'
               '    {\n'
               "        'patient_id': {\n"
               "            'personal': {'name': 'John', 'age': 45, 'gender': 'M'},\n"
               "            'medical': {'allergies': ['penicillin'], 'blood_type': 'O+'},\n"
               "            'visits': [{'date': '2024-01-15', 'diagnosis': 'Hypertension'}]\n"
               '        }\n'
               '    }\n'
               '    \n'
               '    Implement:\n'
               '    1. Add new patient\n'
               '    2. Update patient information\n'
               '    3. Search patients by blood type\n'
               '    4. Get patient visit history\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q1.9',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'reasoning',
  'title': 'Dictionary key eligibility',
  'question': "What types of objects can be used as dictionary keys in Python? Why can't you use a "
              'list of patient symptoms as a dictionary key, but you can use a tuple of symptoms? '
              'Explain with healthcare examples.',
  'answer': 'Keys must be hashable: their hash must remain stable for their lifetime and equality '
            'must be well-defined. Lists are mutable and unhashable; a tuple is hashable only when '
            'all of its members are hashable, making a tuple of symptom strings suitable.',
  'learn_intent': 'Identify hashability as the requirement for dictionary keys.',
  'base_concepts': ['hash', 'equality', 'mutability', 'tuple', 'TypeError'],
  'topic_deepdive': "<p>A dictionary records a key's hash when inserting it. A mutable list could "
                    'change afterwards, invalidating its lookup location.</p><p>A tuple is '
                    'eligible only when all of its members are hashable, such as symptom '
                    'strings.</p>',
  'interview_qa': [{'q': 'Is every tuple hashable?',
                    'a': 'No; a tuple containing a list is unhashable.'},
                   {'q': 'Why do mutable keys break dicts?',
                    'a': 'Their changed hash/equality would make lookups inconsistent.'}],
  'subsection': 'Dictionary Operations',
  'prompt_full': "What types of objects can be used as dictionary keys in Python? Why can't you "
                 'use a list of patient symptoms as a dictionary key, but you can use a tuple of '
                 'symptoms? Explain with healthcare examples.',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q1.10',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'reasoning',
  'title': 'get versus subscription',
  'question': "What's the difference between patient_record.get('blood_type', 'Unknown') and "
              "patient_record['blood_type'] when accessing potentially missing medical data? When "
              'would each approach be appropriate in a healthcare system?',
  'answer': 'get returns a default (or None) without raising, useful for optional fields where '
            'missingness is handled deliberately. Subscription raises KeyError and is better for '
            'required data because it exposes an invalid record early; do not silently turn '
            "mandatory clinical data into 'Unknown'.",
  'learn_intent': 'Choose missing-data access behavior deliberately rather than hiding invalid '
                  'records.',
  'base_concepts': ['KeyError', 'dict.get', 'default values', 'required fields', 'None'],
  'topic_deepdive': '<p>Subscription communicates that a field must exist and raises KeyError if '
                    'the record violates its contract.</p><p>get is appropriate for optional data, '
                    'but its default must not masquerade as a verified blood type.</p>',
  'interview_qa': [{'q': 'What does get return with no default?', 'a': 'None.'},
                   {'q': 'When is KeyError useful?',
                    'a': 'When a required record field is absent and should halt processing.'}],
  'subsection': 'Dictionary Operations',
  'prompt_full': "What's the difference between patient_record.get('blood_type', 'Unknown') and "
                 "patient_record['blood_type'] when accessing potentially missing medical data? "
                 'When would each approach be appropriate in a healthcare system?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q1.11',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'coding',
  'title': 'Drug interaction checker',
  'question': 'Implement a drug interaction checker using sets:',
  'answer': 'Normalize drug names before lookup and intersect the candidate interaction set with '
            'current medications. Treat this as an educational alert only: production interaction '
            'checks need normalized drug vocabularies, dosage/context, provenance, and clinician '
            'review.',
  'learn_intent': 'Use set intersection to detect overlapping medications efficiently.',
  'base_concepts': ['set intersection',
                    'normalization',
                    'dictionary lookup',
                    'case folding',
                    'domain validation'],
  'topic_deepdive': '<p>Interaction lookup identifies drugs that conflict with the candidate '
                    'medication; set intersection finds which of those are currently '
                    'taken.</p><p>Educational string matching is not prescribing logic: real '
                    'systems need normalized drug codes, dose, route, and clinician review.</p>',
  'interview_qa': [{'q': 'Why normalize medication names?',
                    'a': 'Aspirin and aspirin should not become different lookup keys.'},
                   {'q': 'What does an empty intersection mean?',
                    'a': 'No interaction was found in this limited database, not proof of '
                         'safety.'}],
  'code_file': 'Q1_11_drug_interactions.py',
  'subsection': 'Set Operations',
  'prompt_full': 'Implement a drug interaction checker using sets:',
  'code_stub': 'def check_drug_interactions(current_medications: set, new_medication: str, \n'
               '                           interaction_db: dict) -> dict:\n'
               '    """\n'
               '    Check for drug interactions before prescribing new medication\n'
               '    \n'
               '    interaction_db = {\n'
               "        'aspirin': {'warfarin', 'heparin'},\n"
               "        'warfarin': {'aspirin', 'vitamin_k'},\n"
               '        ...\n'
               '    }\n'
               '    \n'
               '    Return: {\n'
               "        'safe': bool,\n"
               "        'interactions': set of conflicting drugs,\n"
               "        'recommendations': list\n"
               '    }\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q1.12',
  'section': '1. Python Datatypes & Built-in Functions',
  'kind': 'reasoning',
  'title': 'Set hashing',
  'question': "How does Python's set implement hashing internally? Why is this crucial for fast "
              'lookups in medical databases containing millions of patient records?',
  'answer': 'A set is a hash table: hash values select sparse-table positions and equality '
            'resolves collisions. Average membership is O(1), but hashes must be stable and '
            'adversarial input can degrade performance; use immutable identifiers and do not claim '
            'a set is a medical database index.',
  'learn_intent': 'Connect hash-table mechanics to fast set membership.',
  'base_concepts': ['hash table',
                    'hashable objects',
                    'collisions',
                    'average O(1)',
                    'set membership'],
  'topic_deepdive': '<p>A set hashes an element to locate a sparse-table slot, then uses equality '
                    'to resolve collisions.</p><p>Average O(1) lookup is useful for identifiers, '
                    'but hash tables are not a substitute for indexed persistent storage.</p>',
  'interview_qa': [{'q': 'Can set lookup be worse than O(1)?',
                    'a': 'Yes, heavy collisions can degrade it.'},
                   {'q': 'Why must hashes be stable?',
                    'a': "Changing an element's hash would make its stored slot unreachable."}],
  'subsection': 'Set Operations',
  'prompt_full': "How does Python's set implement hashing internally? Why is this crucial for fast "
                 'lookups in medical databases containing millions of patient records?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q2.1',
  'section': '2. Typing',
  'kind': 'coding',
  'title': 'Typed patient validation',
  'question': 'Create a strongly-typed patient data validation system:',
  'answer': 'Type hints document and enable static checking but runtime validation must still '
            'check values. Validate identifiers, clinical ranges, enum membership, non-empty '
            'vitals, and the structure of an optional contact; never use annotations alone as '
            'validation.',
  'learn_intent': 'Combine annotations with runtime validation of clinical value ranges.',
  'base_concepts': ['dataclass', 'Enum', 'Optional', 'runtime validation', 'type hints'],
  'topic_deepdive': '<p>Annotations help static tools but do not reject malformed API input at '
                    'runtime.</p><p>A frozen VitalSigns dataclass records a clear shape; '
                    'validation should check both type intent and plausible value ranges.</p>',
  'interview_qa': [{'q': 'Do type hints enforce age limits?',
                    'a': 'No; code or a validation library must enforce them.'},
                   {'q': 'Why use an Enum for blood type?',
                    'a': 'It prevents arbitrary spelling variants from entering the typed model.'}],
  'code_file': 'Q2_1_typed_validation.py',
  'subsection': '',
  'prompt_full': 'Create a strongly-typed patient data validation system:',
  'code_stub': 'from typing import List, Dict, Optional, Union, Tuple\n'
               'from dataclasses import dataclass\n'
               'from enum import Enum\n'
               '\n'
               'class BloodType(Enum):\n'
               '    A_POS = "A+"\n'
               '    A_NEG = "A-"\n'
               '    B_POS = "B+"\n'
               '    B_NEG = "B-"\n'
               '    AB_POS = "AB+"\n'
               '    AB_NEG = "AB-"\n'
               '    O_POS = "O+"\n'
               '    O_NEG = "O-"\n'
               '\n'
               '@dataclass\n'
               'class VitalSigns:\n'
               '    systolic: int\n'
               '    diastolic: int\n'
               '    temperature: float\n'
               '    heart_rate: int\n'
               '    timestamp: str\n'
               '\n'
               'def validate_patient_data(patient_id: str, \n'
               '                         age: int,\n'
               '                         blood_type: BloodType,\n'
               '                         vitals: List[VitalSigns],\n'
               '                         emergency_contact: Optional[Dict[str, str]] = None) -> '
               'bool:\n'
               '    """\n'
               '    Validate patient data with proper type hints\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q2.2',
  'section': '2. Typing',
  'kind': 'reasoning',
  'title': 'Python hints versus Java types',
  'question': "How do Python's type hints differ from Java's static typing? What are the benefits "
              'of using type hints in a large healthcare codebase with multiple developers?',
  'answer': 'Java normally enforces declared types at compile time; Python annotations are '
            'metadata and require tools such as pyright or mypy plus runtime validation for '
            'external data. They clarify contracts, catch integration mismatches, improve '
            'refactoring, and document nullable clinical fields.',
  'learn_intent': "Explain Python's opt-in static analysis model accurately.",
  'base_concepts': ['static typing', 'type annotations', 'mypy', 'pyright', 'runtime data'],
  'topic_deepdive': "<p>Java's compiler enforces declared type compatibility; Python annotations "
                    'are metadata used by optional tooling.</p><p>Large Python teams gain safer '
                    'refactoring and clearer interfaces, but still validate JSON, databases, and '
                    'user input at runtime.</p>',
  'interview_qa': [{'q': 'Can Python run code with wrong annotations?',
                    'a': 'Yes, unless additional runtime validation is used.'},
                   {'q': 'What is a benefit of strict checking?',
                    'a': 'It finds incompatible interfaces before an integration test.'}],
  'subsection': '',
  'prompt_full': "How do Python's type hints differ from Java's static typing? What are the "
                 'benefits of using type hints in a large healthcare codebase with multiple '
                 'developers?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q3.1',
  'section': '3. Operators',
  'kind': 'coding',
  'title': 'BMI and dosage arithmetic',
  'question': 'Calculate BMI and medication dosage using various arithmetic operators:',
  'answer': 'Guard height and dosage against zero, calculate BMI as kg/m², apply the 10% reduction '
            'only when age exceeds 65, and choose a stated policy for fractional days (floor, '
            'ceiling, or precise value).',
  'learn_intent': 'Apply arithmetic safely, including zero guards and dosage policy.',
  'base_concepts': ['arithmetic operators',
                    'precedence',
                    'division by zero',
                    'conditionals',
                    'floor division'],
  'topic_deepdive': '<p>BMI is weight divided by height squared, so height must be positive. '
                    'Dosage rules should be applied once and documented.</p><p>Days supply needs a '
                    'rounding policy: floor means complete doses only, while ceiling means enough '
                    'supply to cover a final partial day.</p>',
  'interview_qa': [{'q': 'Why not divide by a zero height?',
                    'a': 'It raises ZeroDivisionError and represents invalid input.'},
                   {'q': 'Is BMI a diagnosis?', 'a': 'No; it is a derived screening measure.'}],
  'code_file': 'Q3_1_medical_calculations.py',
  'subsection': 'Arithmetic Operators',
  'prompt_full': 'Calculate BMI and medication dosage using various arithmetic operators:',
  'code_stub': 'def medical_calculations(weight_kg: float, height_m: float, \n'
               '                        base_dosage_mg: float, patient_age: int) -> dict:\n'
               '    """\n'
               '    Calculate:\n'
               '    1. BMI using weight and height\n'
               '    2. Adjusted medication dosage (reduce by 10% for patients over 65)\n'
               '    3. Days supply if total medication is 1000mg and dosage is calculated above\n'
               '    4. Whether patient is in healthy BMI range (18.5-24.9)\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q3.2',
  'section': '3. Operators',
  'kind': 'coding',
  'title': 'Vital-sign triage',
  'question': 'Create a patient triage system using comparison operators:',
  'answer': 'Check critical criteria before urgent criteria and compare systolic and diastolic '
            'components explicitly rather than tuple ordering. This is a programming exercise, not '
            'a safe clinical triage protocol.',
  'learn_intent': 'Order compound comparison rules so critical conditions win.',
  'base_concepts': ['comparison operators',
                    'and/or',
                    'tuple unpacking',
                    'rule precedence',
                    'short-circuiting'],
  'topic_deepdive': '<p>Compare systolic and diastolic values separately; tuple comparison is '
                    'lexicographic and can hide the intended rule.</p><p>Check critical criteria '
                    'first, then urgent criteria, so an emergency is not downgraded by a later '
                    'branch.</p>',
  'interview_qa': [{'q': 'What does short-circuiting do here?',
                    'a': 'It stops evaluating an OR expression once a true emergency criterion is '
                         'found.'},
                   {'q': 'Is this safe clinical triage?',
                    'a': 'No; it is a programming exercise with simplified thresholds.'}],
  'code_file': 'Q3_2_triage.py',
  'subsection': 'Comparison and Logical Operators',
  'prompt_full': 'Create a patient triage system using comparison operators:',
  'code_stub': 'def triage_patient(temperature: float, blood_pressure: tuple, \n'
               '                  heart_rate: int, is_conscious: bool, \n'
               '                  pain_level: int) -> str:\n'
               '    """\n'
               '    Determine patient priority based on vital signs:\n'
               '    - Critical: Temp > 104°F OR BP > (180, 120) OR Heart rate > 120 OR '
               'unconscious\n'
               '    - Urgent: Temp > 101°F OR BP > (140, 90) OR Pain > 7\n'
               '    - Standard: All other cases\n'
               '    \n'
               '    Use appropriate comparison and logical operators\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q3.3',
  'section': '3. Operators',
  'kind': 'coding',
  'title': 'Bitwise permissions',
  'question': 'Implement a patient permission system using bitwise operators:',
  'answer': 'Combine flags with |, clear a flag with &= ~flag, and test with (permissions & flag) '
            '== flag. Validate that supplied flags are from the supported mask; authorization also '
            'needs identity, auditing, and server-side enforcement.',
  'learn_intent': 'Represent independent access rights with a bit mask.',
  'base_concepts': ['bitwise OR', 'bitwise AND', 'bitwise NOT', 'flags', 'authorization'],
  'topic_deepdive': '<p>Each permission owns one bit. OR combines rights, AND tests a right, and '
                    'AND with NOT clears one.</p><p>A bit mask is compact but only represents '
                    'capability flags; authentication, ownership, and audit logging remain '
                    'separate concerns.</p>',
  'interview_qa': [{'q': 'How is READ and WRITE represented?', 'a': '1 | 2, which is 3.'},
                   {'q': 'Why use == permission after AND?',
                    'a': 'It confirms every requested bit is present.'}],
  'code_file': 'Q3_3_permissions.py',
  'subsection': 'Bitwise Operators',
  'prompt_full': 'Implement a patient permission system using bitwise operators:',
  'code_stub': 'class PatientPermissions:\n'
               '    """\n'
               '    Use bitwise operators to manage patient data access permissions:\n'
               '    READ = 1 (001)\n'
               '    WRITE = 2 (010)  \n'
               '    DELETE = 4 (100)\n'
               '    """\n'
               '    READ = 1\n'
               '    WRITE = 2\n'
               '    DELETE = 4\n'
               '    \n'
               '    def __init__(self, permissions: int = 0):\n'
               '        self.permissions = permissions\n'
               '    \n'
               '    def add_permission(self, permission: int):\n'
               '        """Add permission using bitwise OR"""\n'
               '        pass\n'
               '    \n'
               '    def remove_permission(self, permission: int):\n'
               '        """Remove permission using bitwise operations"""\n'
               '        pass\n'
               '    \n'
               '    def has_permission(self, permission: int) -> bool:\n'
               '        """Check if permission exists using bitwise AND"""\n'
               '        pass',
  'expected_output': ''},
 {'id': 'Q3.4',
  'section': '3. Operators',
  'kind': 'coding',
  'title': 'Patient eligibility',
  'question': 'Implement patient eligibility checker:',
  'answer': 'Normalize free-text values, use set intersections for any-match rules, and use `is '
            'None` rather than equality for absent optional values. Return separate decision facts '
            'rather than concealing why eligibility failed.',
  'learn_intent': 'Use membership and identity operators with correct clinical data semantics.',
  'base_concepts': ['in', 'not in', 'is None', 'set intersection', 'optional values'],
  'topic_deepdive': '<p>Membership answers whether a symptom or insurer appears in a collection; '
                    'set intersection efficiently checks any overlap.</p><p>Use `is None` for '
                    'missing optional history, not `== None`, which can invoke surprising custom '
                    'equality.</p>',
  'interview_qa': [{'q': 'Why convert symptoms to a set?',
                    'a': 'It makes overlap checks clear and efficient.'},
                   {'q': 'Does no critical symptom prove eligibility?',
                    'a': 'No; it is only one decision fact.'}],
  'code_file': 'Q3_4_eligibility.py',
  'subsection': 'Membership and Identity Operators',
  'prompt_full': 'Implement patient eligibility checker:',
  'code_stub': 'def check_patient_eligibility(patient_age: int, symptoms: list, \n'
               '                             insurance_types: list, medical_history: list) -> '
               'dict:\n'
               '    """\n'
               "    Use 'in' and 'not in' operators to check:\n"
               '    1. If patient has any critical symptoms\n'
               "    2. If patient's insurance is accepted\n"
               '    3. If patient has conflicting medical history\n'
               '    \n'
               "    Use 'is' and 'is not' for None checks on optional data\n"
               '    """\n'
               "    critical_symptoms = ['chest_pain', 'difficulty_breathing', 'severe_bleeding']\n"
               "    accepted_insurance = ['medicare', 'aetna', 'bcbs', 'cigna']\n"
               '    \n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q3.5',
  'section': '3. Operators',
  'kind': 'coding',
  'title': 'Walrus vital processing',
  'question': 'Use walrus operator for efficient patient data processing:',
  'answer': 'Assignment expressions should bind a value that is immediately tested or reused, '
            'keeping the condition readable. Use them sparingly; explicit intermediate variables '
            'are clearer when a clinical rule is non-trivial.',
  'learn_intent': 'Use := only where binding and testing the same derived value improves clarity.',
  'base_concepts': ['assignment expressions',
                    'walrus operator',
                    'loop',
                    'truthy tests',
                    'local variables'],
  'topic_deepdive': '<p>The walrus operator assigns an intermediate result inside an expression, '
                    'avoiding repeated BMI or medication-count calculations.</p><p>It is best for '
                    'short conditions; a named statement is clearer when the clinical rule needs '
                    'explanation.</p>',
  'interview_qa': [{'q': 'What does := return?', 'a': 'The value assigned to its target.'},
                   {'q': 'Why avoid repeated BMI calculation?',
                    'a': 'It reduces duplicated work and keeps the tested value consistent.'}],
  'code_file': 'Q3_5_walrus_vitals.py',
  'subsection': 'Walrus Operator',
  'prompt_full': 'Use walrus operator for efficient patient data processing:',
  'code_stub': 'def process_patient_vitals(patients_data: list) -> list:\n'
               '    """\n'
               '    Use walrus operator to efficiently process and filter patient data:\n'
               '    - Calculate BMI and filter patients with BMI > 30\n'
               '    - Process temperature readings and flag fever cases\n'
               '    - Extract medication counts and identify patients with > 5 medications\n'
               '    """\n'
               '    results = []\n'
               '    \n'
               '    for patient in patients_data:\n'
               '        # Use walrus operator for BMI calculation and filtering\n'
               '        # Use walrus operator for temperature processing\n'
               '        # Use walrus operator for medication counting\n'
               '        pass\n'
               '    \n'
               '    return results',
  'expected_output': ''},
 {'id': 'Q4.1',
  'section': '4. Conditional Flow Control',
  'kind': 'coding',
  'title': 'Diagnosis workflow',
  'question': 'Create a comprehensive patient diagnosis workflow:',
  'answer': 'Make rules ordered, explicit, and testable; a function should return a structured '
            'assessment rather than pretend to diagnose. Monitoring loops must have bounded '
            'iterations and stable exit conditions.',
  'learn_intent': 'Build ordered branches and bounded loops for an explicit decision workflow.',
  'base_concepts': ['if/elif/else', 'nested conditions', 'while loops', 'for loops', 'break'],
  'topic_deepdive': '<p>Decision trees should prioritize emergencies before chronic and routine '
                    'paths, and return a structured action.</p><p>Monitoring loops need a finite '
                    'duration and a documented stable-state exit rule; unbounded polling is a '
                    'reliability bug.</p>',
  'interview_qa': [{'q': 'Why check emergency symptoms first?',
                    'a': 'Priority ordering prevents dangerous conditions being hidden by a later '
                         'rule.'},
                   {'q': 'What should a loop return?',
                    'a': 'Observations or alerts, not an unsupported diagnosis.'}],
  'code_file': 'Q4_1_diagnosis_flow.py',
  'subsection': '',
  'prompt_full': 'Create a comprehensive patient diagnosis workflow:',
  'code_stub': 'def diagnose_patient(symptoms: list, vital_signs: dict, \n'
               '                    medical_history: list, lab_results: dict) -> dict:\n'
               '    """\n'
               '    Implement a diagnosis decision tree using if-else, nested conditions:\n'
               '    \n'
               '    Priority flow:\n'
               '    1. Check for emergency conditions first\n'
               '    2. Evaluate chronic condition indicators\n'
               '    3. Consider common ailments\n'
               '    4. Default to further testing required\n'
               '    \n'
               '    Use nested if-else appropriately for complex medical decision making\n'
               '    """\n'
               '    pass\n'
               '\n'
               'def patient_monitoring_loop(patient_id: str, monitoring_duration_hours: int):\n'
               '    """\n'
               '    Use while loop to simulate patient vital signs monitoring\n'
               '    - Check vitals every 30 minutes\n'
               '    - Alert if vitals go outside normal ranges\n'
               '    - Break if patient is stable for 2 consecutive hours\n'
               '    """\n'
               '    pass\n'
               '\n'
               'def daily_medication_schedule(patient_medications: dict):\n'
               '    """\n'
               '    Use for loop to generate daily medication reminders\n'
               '    - Iterate through medication times\n'
               '    - Handle special cases (meals, sleep time)\n'
               '    - Generate patient-friendly schedule\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q5.1',
  'section': '5. Comprehensions',
  'kind': 'coding',
  'title': 'Healthcare comprehensions',
  'question': 'Implement efficient data processing using comprehensions:',
  'answer': 'Comprehensions fit simple transformations; use a generator for lazy high-risk '
            'processing. Avoid embedding complex clinical logic in a comprehension because named '
            'predicates are easier to audit and test.',
  'learn_intent': 'Match each comprehension form to its output shape and use generators lazily.',
  'base_concepts': ['list comprehension',
                    'dict comprehension',
                    'set comprehension',
                    'generator expression',
                    'nested loops'],
  'topic_deepdive': '<p>A list comprehension collects matching patients, a dict maps IDs to latest '
                    'readings, and a set removes duplicate medications.</p><p>A generator defers '
                    'high-risk records until consumed, which is useful for streams too large to '
                    'materialize.</p>',
  'interview_qa': [{'q': 'Why is a generator single-use?',
                    'a': 'Iteration advances and eventually exhausts its suspended frame.'},
                   {'q': 'When should a comprehension become a function?',
                    'a': 'When its predicate or transformation is too complex to read inline.'}],
  'code_file': 'Q5_1_comprehensions.py',
  'subsection': '',
  'prompt_full': 'Implement efficient data processing using comprehensions:',
  'code_stub': 'def medical_data_processing(patient_records: list) -> dict:\n'
               '    """\n'
               '    Use different comprehensions to process medical data:\n'
               '    \n'
               '    1. List comprehension: Extract all patients with diabetes\n'
               '    2. Dictionary comprehension: Map patient IDs to their latest vital signs\n'
               '    3. Set comprehension: Get unique medications across all patients\n'
               '    4. Generator expression: Memory-efficient processing of large patient '
               'datasets\n'
               '    """\n'
               '    \n'
               '    # List comprehension for diabetic patients\n'
               '    diabetic_patients = # Your code here\n'
               '    \n'
               '    # Dictionary comprehension for latest vitals\n'
               '    latest_vitals = # Your code here\n'
               '    \n'
               '    # Set comprehension for unique medications  \n'
               '    unique_medications = # Your code here\n'
               '    \n'
               '    # Generator for memory-efficient processing\n'
               '    def high_risk_patients():\n'
               '        # Generator expression here\n'
               '        pass\n'
               '    \n'
               '    return {\n'
               "        'diabetic_patients': diabetic_patients,\n"
               "        'latest_vitals': latest_vitals,\n"
               "        'unique_medications': unique_medications,\n"
               "        'high_risk_generator': high_risk_patients()\n"
               '    }',
  'expected_output': ''},
 {'id': 'Q5.2',
  'section': '5. Comprehensions',
  'kind': 'reasoning',
  'title': 'Generator state',
  'question': 'How does a generator expression maintain state internally between iterations? Why '
              'would you use a generator instead of a list comprehension when processing millions '
              'of patient records?',
  'answer': 'A generator stores its suspended frame, instruction position, and local bindings '
            'between next calls. It streams values and keeps memory near O(1) beyond the source, '
            'unlike a list comprehension that materializes all results; it is single-use and may '
            'defer errors.',
  'learn_intent': 'Explain generator frames and the memory trade-off of laziness.',
  'base_concepts': ['yield', 'generator frame', 'next', 'lazy evaluation', 'memory complexity'],
  'topic_deepdive': '<p>A generator keeps its instruction position and local variables in a '
                    'suspended frame between next calls.</p><p>It reduces peak memory for millions '
                    'of records, but delays computation and errors until iteration.</p>',
  'interview_qa': [{'q': 'Does a generator calculate all values immediately?',
                    'a': 'No, it evaluates values on demand.'},
                   {'q': 'Can you iterate it twice?', 'a': 'Not after it has been exhausted.'}],
  'subsection': '',
  'prompt_full': 'How does a generator expression maintain state internally between iterations? '
                 'Why would you use a generator instead of a list comprehension when processing '
                 'millions of patient records?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q6.1',
  'section': '6. Python Functions',
  'kind': 'coding',
  'title': 'Flexible appointments',
  'question': 'Design a flexible patient appointment scheduling function:',
  'answer': 'Capture variable details deliberately, validate required identifiers, and return a '
            'normalized appointment record. Positional-only prevents callers binding the '
            'identifier by name; keyword-only keeps optional safety-sensitive fields '
            'self-documenting.',
  'learn_intent': 'Use *args and **kwargs without losing a stable public API.',
  'base_concepts': ['positional-only parameters',
                    'keyword-only parameters',
                    '*args',
                    '**kwargs',
                    'function signatures'],
  'topic_deepdive': '<p>*args captures variable appointment details; **kwargs captures named '
                    'scheduling options. Normalize both into explicit record fields.</p><p>The '
                    'slash makes patient_id positional-only, while the star forces sensitive '
                    'optional fields to be named at the call site.</p>',
  'interview_qa': [{'q': 'Why make blood_type keyword-only?',
                    'a': 'Named calls make optional medical fields clearer and harder to '
                         'misorder.'},
                   {'q': 'What does / mean in a signature?',
                    'a': 'Parameters before it cannot be passed by keyword.'}],
  'code_file': 'Q6_1_appointments.py',
  'subsection': 'Positional & Keyword Arguments',
  'prompt_full': 'Design a flexible patient appointment scheduling function:',
  'code_stub': 'def schedule_appointment(patient_id, doctor_id, *appointment_details, \n'
               '                        **scheduling_options):\n'
               '    """\n'
               '    Create flexible appointment scheduling:\n'
               '    - Required: patient_id, doctor_id\n'
               '    - Variable positional: date, time, duration, appointment_type\n'
               '    - Keyword arguments: priority, notes, insurance_verification, etc.\n'
               '    \n'
               '    Handle different calling patterns:\n'
               '    schedule_appointment("P123", "D456", "2024-02-15", "10:00")\n'
               '    schedule_appointment("P123", "D456", priority="urgent", notes="follow-up")\n'
               '    """\n'
               '    pass\n'
               '\n'
               'def update_patient_record(patient_id, /, name=None, age=None, *, \n'
               '                         blood_type=None, emergency_contact=None):\n'
               '    """\n'
               '    Demonstrate positional-only and keyword-only arguments\n'
               '    - patient_id must be positional\n'
               '    - blood_type and emergency_contact must be keyword-only\n'
               '    """\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q6.2',
  'section': '6. Python Functions',
  'kind': 'coding',
  'title': 'Recursive family risk',
  'question': 'Implement recursive functions for medical data structures:',
  'answer': 'Use a visited set to prevent cycles and define whether multiple paths are additive, '
            'capped, or deduplicated. Recursive traversal is clear for a small graph; production '
            'systems often use iterative traversal and clinically validated risk models.',
  'learn_intent': 'Traverse recursive family and interaction graphs while preventing cycles.',
  'base_concepts': ['recursion', 'base case', 'visited set', 'graphs', 'call stack'],
  'topic_deepdive': '<p>Each recursive call moves to a parent or interacting drug, and the base '
                    'case stops at unknown or already visited nodes.</p><p>A visited set prevents '
                    'cyclic relationships from causing infinite recursion or duplicate '
                    'traversal.</p>',
  'interview_qa': [{'q': 'Why is a mutable default visited set dangerous?',
                    'a': 'It would be shared across calls; initialize it with None instead.'},
                   {'q': 'When prefer iterative traversal?',
                    'a': 'For deep or large graphs that risk recursion-depth limits.'}],
  'code_file': 'Q6_2_family_risk.py',
  'subsection': 'Recursion',
  'prompt_full': 'Implement recursive functions for medical data structures:',
  'code_stub': 'def calculate_family_risk_score(family_tree: dict, condition: str, \n'
               '                               current_person: str, generation: int = 0) -> '
               'float:\n'
               '    """\n'
               '    Recursively calculate genetic risk score based on family history:\n'
               '    \n'
               '    family_tree = {\n'
               "        'john': {\n"
               "            'conditions': ['diabetes', 'hypertension'],\n"
               "            'parents': ['mary', 'robert'],\n"
               "            'children': ['jane', 'mike']\n"
               '        },\n'
               "        'mary': {\n"
               "            'conditions': ['diabetes'],\n"
               "            'parents': [],\n"
               "            'children': ['john']\n"
               '        }\n'
               '    }\n'
               '    \n'
               '    Risk scoring:\n'
               '    - Direct parent/child: 0.5 * base_risk\n'
               '    - Grandparent/grandchild: 0.25 * base_risk  \n'
               '    - Great-grandparent: 0.125 * base_risk\n'
               '    """\n'
               '    pass\n'
               '\n'
               'def find_medication_interactions(drug: str, interaction_tree: dict, \n'
               '                               visited: set = None) -> set:\n'
               '    """\n'
               '    Recursively find all possible drug interactions in a complex network\n'
               '    """\n'
               '    if visited is None:\n'
               '        visited = set()\n'
               '    \n'
               '    # Implement recursive interaction detection\n'
               '    pass',
  'expected_output': ''},
 {'id': 'Q6.3',
  'section': '6. Python Functions',
  'kind': 'coding',
  'title': 'Lambda lab processing',
  'question': 'Use lambda functions for medical data processing:',
  'answer': 'Keep lambdas short: define a reusable deviation calculation and use it as the sorting '
            'key. Include bounds correctly and retain the original record with its computed '
            'severity for traceability.',
  'learn_intent': 'Use small lambdas as function arguments and preserve severity logic.',
  'base_concepts': ['lambda', 'map', 'filter', 'sorted key', 'higher-order functions'],
  'topic_deepdive': '<p>filter selects abnormal records, map derives severity, and sorted uses the '
                    'same severity function as its key.</p><p>A lambda should remain short; name a '
                    'helper when the deviation calculation gains domain complexity.</p>',
  'interview_qa': [{'q': 'Why reuse one deviation formula?',
                    'a': 'It keeps filtering, scoring, and ordering consistent.'},
                   {'q': "What should sorted's key return?",
                    'a': 'A comparable severity value for each lab record.'}],
  'code_file': 'Q6_3_lab_lambda.py',
  'subsection': 'Recursion',
  'prompt_full': 'Use lambda functions for medical data processing:',
  'code_stub': 'def process_lab_results(lab_data: list) -> dict:\n'
               '    """\n'
               '    Use lambda functions with map, filter, and sorted for lab result processing:\n'
               '    \n'
               '    lab_data = [\n'
               "        {'test': 'glucose', 'value': 120, 'normal_range': (70, 100)},\n"
               "        {'test': 'cholesterol', 'value': 180, 'normal_range': (0, 200)},\n"
               "        {'test': 'hemoglobin', 'value': 12.5, 'normal_range': (12, 16)}\n"
               '    ]\n'
               '    """\n'
               '    \n'
               '    # Lambda to check if result is abnormal\n'
               '    abnormal_results = list(filter(# lambda here, lab_data))\n'
               '    \n'
               '    # Lambda to calculate how far from normal range\n'
               '    severity_scores = list(map(# lambda here, lab_data))\n'
               '    \n'
               '    # Lambda for custom sorting by severity\n'
               '    sorted_by_priority = sorted(lab_data, key=# lambda here)\n'
               '    \n'
               '    return {\n'
               "        'abnormal': abnormal_results,\n"
               "        'severity_scores': severity_scores,\n"
               "        'priority_order': sorted_by_priority\n"
               '    }',
  'expected_output': ''},
 {'id': 'Q6.4',
  'section': '6. Python Functions',
  'kind': 'coding',
  'title': 'Scope management',
  'question': 'Demonstrate scope management in medical system:',
  'answer': 'Read globals without `global`; use the declaration only when rebinding a module name. '
            'Prefer passing configuration or using an object in production because mutation of '
            'global state hinders tests and concurrent requests.',
  'learn_intent': 'Apply LEGB scope rules and avoid unnecessary global rebinding.',
  'base_concepts': ['LEGB', 'global variables', 'local variables', 'closures', 'mutable objects'],
  'topic_deepdive': '<p>Nested functions can read module configuration without a global '
                    'declaration. `global` is only needed to rebind a module-level '
                    'name.</p><p>Mutating global configuration complicates tests and concurrency, '
                    'so pass configuration explicitly when possible.</p>',
  'interview_qa': [{'q': 'Does changing a dict item require global?',
                    'a': 'No; global is required for rebinding the name, not mutating its object.'},
                   {'q': 'Why keep processing values local?',
                    'a': 'Local state limits unintended cross-request effects.'}],
  'code_file': 'Q6_4_scope.py',
  'subsection': 'Local and Global Scope',
  'prompt_full': 'Demonstrate scope management in medical system:',
  'code_stub': '# Global configuration\n'
               'HOSPITAL_CONFIG = {\n'
               "    'max_patients_per_doctor': 50,\n"
               "    'emergency_threshold_temp': 104.0,\n"
               "    'default_appointment_duration': 30\n"
               '}\n'
               '\n'
               'def patient_management_system():\n'
               '    """\n'
               '    Demonstrate proper scope management:\n'
               '    - Global variables for hospital configuration\n'
               '    - Local variables for patient processing\n'
               '    - Proper use of global keyword when needed\n'
               '    """\n'
               '    \n'
               '    def assign_doctor(patient_severity: str):\n'
               '        # Access global config appropriately\n'
               '        # Use local variables for calculations\n'
               '        # Modify global state when necessary (use global keyword)\n'
               '        pass\n'
               '    \n'
               '    def update_hospital_capacity(new_limit: int):\n'
               '        # Properly modify global configuration\n'
               '        pass\n'
               '    \n'
               '    return assign_doctor, update_hospital_capacity',
  'expected_output': ''},
 {'id': 'Q6.5',
  'section': '6. Python Functions',
  'kind': 'reasoning',
  'title': 'LEGB and Java scope',
  'question': 'Explain the difference between local and global scope in Python compared to Java. '
              'How does the LEGB rule apply when accessing hospital configuration data from nested '
              'functions?',
  'answer': 'Python resolves names Local, Enclosing, Global, then Builtins. Java is statically '
            'scoped too but fields are accessed through class/instance context; nested Python '
            'functions close over enclosing names and need `nonlocal` to rebind them, while '
            '`global` targets the module.',
  'learn_intent': 'Reason about local, enclosing, global, and builtin name resolution.',
  'base_concepts': ['LEGB', 'nonlocal', 'global', 'closures', 'static scope'],
  'topic_deepdive': '<p>Python looks in Local, Enclosing, Global, then Builtins scopes. A nested '
                    'diagnosis rule can read an enclosing threshold.</p><p>Use nonlocal to rebind '
                    'the enclosing binding and global only for module-level bindings; Java uses '
                    'lexical scope but has different class/field syntax.</p>',
  'interview_qa': [{'q': 'What scope wins over a global?',
                    'a': 'A local binding with the same name.'},
                   {'q': 'When use nonlocal?',
                    'a': 'When a nested function must rebind a variable in its enclosing '
                         'function.'}],
  'subsection': 'Local and Global Scope',
  'prompt_full': 'Explain the difference between local and global scope in Python compared to '
                 'Java. How does the LEGB rule apply when accessing hospital configuration data '
                 'from nested functions?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q7.1',
  'section': '7. Built-in Functions',
  'kind': 'coding',
  'title': 'Built-in medical analysis',
  'question': 'Comprehensive use of built-in functions for medical data:',
  'answer': 'Use each builtin where it improves clarity: reduce needs an empty-input policy, zip '
            'truncates to the shortest input, and id is diagnostic only. Return structured results '
            'and avoid treating simplistic risk sorting as clinical decision support.',
  'learn_intent': 'Choose built-ins for transformation, aggregation, pairing, and inspection.',
  'base_concepts': ['map', 'filter', 'zip', 'reduce', 'sorted', 'enumerate'],
  'topic_deepdive': '<p>map and filter express simple transformations, zip pairs parallel '
                    'iterables but truncates to the shortest, and reduce needs an empty-input '
                    'policy.</p><p>type and id are debugging tools; id is not a stable patient '
                    'identifier or persisted key.</p>',
  'interview_qa': [{'q': "What is zip's truncation behavior?",
                    'a': 'It stops at the shortest input iterable.'},
                   {'q': 'Why guard reduce on empty records?',
                    'a': 'reduce without an initializer raises TypeError on an empty sequence.'}],
  'code_file': 'Q7_1_builtins_analysis.py',
  'subsection': '',
  'prompt_full': 'Comprehensive use of built-in functions for medical data:',
  'code_stub': 'def medical_data_analysis(patient_records: list, lab_results: list) -> dict:\n'
               '    """\n'
               '    Use various built-in functions to analyze medical data:\n'
               '    \n'
               '    patient_records = [\n'
               "        {'id': 'P001', 'age': 45, 'medications': ['aspirin', 'lisinopril']},\n"
               "        {'id': 'P002', 'age': 67, 'medications': ['metformin', 'aspirin']},\n"
               '    ]\n'
               '    \n'
               '    lab_results = [\n'
               "        ('P001', [120, 80, 98.6]),  # glucose, bp_sys, temp\n"
               "        ('P002', [140, 90, 99.1]),\n"
               '    ]\n'
               '    """\n'
               '    \n'
               '    # Use map() to extract patient ages\n'
               '    ages = list(map(# Your code here))\n'
               '    \n'
               '    # Use filter() to find elderly patients (age > 65)\n'
               '    elderly = list(filter(# Your code here))\n'
               '    \n'
               '    # Use zip() to combine patient data with lab results\n'
               '    combined_data = list(zip(# Your code here))\n'
               '    \n'
               '    # Use enumerate() to process patients with index\n'
               '    indexed_patients = list(enumerate(# Your code here))\n'
               '    \n'
               '    # Use reduce() to find patient with most medications\n'
               '    from functools import reduce\n'
               '    most_medications = reduce(# Your code here)\n'
               '    \n'
               '    # Use sorted() with custom key for complex sorting\n'
               '    sorted_by_risk = sorted(# Your code here)\n'
               '    \n'
               '    # Use min/max for vital statistics\n'
               '    min_age = min(# Your code here)\n'
               '    max_temp = max(# Your code here)\n'
               '    \n'
               '    # Use type() and id() for debugging patient data issues\n'
               '    data_types = {pid: type(data) for pid, data in # Your code here}\n'
               '    \n'
               '    # Use range() for generating appointment time slots\n'
               '    time_slots = list(range(# Your code here))\n'
               '    \n'
               '    return {\n'
               "        'ages': ages,\n"
               "        'elderly_patients': elderly,\n"
               "        'combined_data': combined_data,\n"
               "        'indexed_patients': indexed_patients,\n"
               "        'patient_most_meds': most_medications,\n"
               "        'risk_sorted': sorted_by_risk,\n"
               "        'statistics': {'min_age': min_age, 'max_temp': max_temp},\n"
               "        'data_types': data_types,\n"
               "        'available_slots': time_slots\n"
               '    }',
  'expected_output': ''},
 {'id': 'Q7.2',
  'section': '7. Built-in Functions',
  'kind': 'reasoning',
  'title': 'Python and Java reduce',
  'question': "Compare Python's reduce() function with Java 8's stream reduce(). How would you use "
              'reduce() to aggregate patient statistics across multiple hospital departments?',
  'answer': 'Both repeatedly combine values with an associative accumulator; Java streams support '
            'parallel reduction only when identity/associativity requirements are met. In Python, '
            'use reduce for a clear binary fold but prefer sum/min/max or a dataclass accumulator '
            'for readable departmental statistics.',
  'learn_intent': 'Compare functional folds while recognizing associativity requirements.',
  'base_concepts': ['reduce', 'accumulator', 'identity value', 'associativity', 'Java streams'],
  'topic_deepdive': '<p>Both Python reduce and Java Stream.reduce combine a sequence with an '
                    'accumulator. Parallel Java reduction requires an associative operation and '
                    'appropriate identity.</p><p>For patient totals, sum or a named accumulator '
                    'can be clearer than an opaque lambda reduce.</p>',
  'interview_qa': [{'q': 'What is an identity for addition?', 'a': 'Zero.'},
                   {'q': 'Why does associativity matter?',
                    'a': 'It allows grouping partial reductions without changing the result.'}],
  'subsection': '',
  'prompt_full': "Compare Python's reduce() function with Java 8's stream reduce(). How would you "
                 'use reduce() to aggregate patient statistics across multiple hospital '
                 'departments?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R1',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'One-item tuple review',
  'question': 'Why is patient_info = (42) an integer while patient_info = (42,) is a tuple? How '
              'does this affect storing single vital sign measurements?',
  'answer': 'The comma creates the tuple; parentheses only group. Choose the scalar unless an '
            'immutable one-element sequence is required by an API.',
  'learn_intent': 'Reinforce the syntax distinction behind singleton tuples.',
  'base_concepts': ['tuple literal', 'comma operator', 'parentheses', 'type inspection'],
  'topic_deepdive': '<p>Parentheses group a scalar expression, while a trailing comma constructs a '
                    'tuple.</p><p>Checking type during debugging quickly exposes accidental '
                    'scalar-versus-sequence API mismatches.</p>',
  'interview_qa': [{'q': 'Which token makes (42,) a tuple?', 'a': 'The comma.'},
                   {'q': 'Why can this break a function?',
                    'a': 'A function expecting an iterable may receive a non-iterable scalar.'}],
  'subsection': '',
  'prompt_full': 'Why is patient_info = (42) an integer while patient_info = (42,) is a tuple? How '
                 'does this affect storing single vital sign measurements?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R2',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'Hashable symptom keys',
  'question': "What makes certain objects hashable and suitable as dictionary keys? Why can't you "
              "use ['symptom1', 'symptom2'] as a key but ('symptom1', 'symptom2') works?",
  'answer': 'Hashable objects have stable hashes and compatible equality. A mutable list can '
            'change after insertion, so it is unhashable; an all-hashable tuple is safe as a '
            'composite key.',
  'learn_intent': 'Reinforce immutable composite keys and hash stability.',
  'base_concepts': ['hashability', 'immutability', 'dict keys', 'tuple', 'list'],
  'topic_deepdive': '<p>A list is mutable and therefore intentionally unhashable. A tuple of '
                    'immutable symptom strings has stable equality and hash behavior.</p><p>Use a '
                    'canonical ordering if symptom combinations must be order-independent.</p>',
  'interview_qa': [{'q': "Does ('cough','fever') equal ('fever','cough')?",
                    'a': 'No; tuple order matters.'},
                   {'q': 'How model unordered symptoms as a key?',
                    'a': 'Use frozenset of normalized symptom codes.'}],
  'subsection': '',
  'prompt_full': "What makes certain objects hashable and suitable as dictionary keys? Why can't "
                 "you use ['symptom1', 'symptom2'] as a key but ('symptom1', 'symptom2') works?",
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R3',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'String interning',
  'question': "How does Python's string interning work? When you have thousands of patient records "
              'with repeated values like "Type 2 Diabetes", how does Python optimize memory usage?',
  'answer': 'CPython may intern some identifiers and literals, but interning is an implementation '
            'optimization—not a storage guarantee. Normalize repeated clinical concepts to '
            'controlled codes in a database instead of depending on object identity or interning.',
  'learn_intent': 'Avoid mistaking CPython interning for a healthcare storage strategy.',
  'base_concepts': ['string interning',
                    'object identity',
                    'string equality',
                    'normalization',
                    'memory profiling'],
  'topic_deepdive': '<p>CPython may intern identifier-like or literal strings, but the behavior is '
                    'an implementation optimization, not an application contract.</p><p>Store '
                    'repeated diagnoses as controlled codes and compare strings with ==, never '
                    'is.</p>',
  'interview_qa': [{'q': 'Can interning be relied on across Python implementations?', 'a': 'No.'},
                   {'q': 'What reduces repeated diagnosis storage reliably?',
                    'a': 'A normalized code/reference model in persistent storage.'}],
  'subsection': '',
  'prompt_full': "How does Python's string interning work? When you have thousands of patient "
                 'records with repeated values like "Type 2 Diabetes", how does Python optimize '
                 'memory usage?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R4',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'Equality and identity',
  'question': "What's the difference between == and is operators? In a healthcare system, when "
              'would you use each to compare patient data?',
  'answer': '== compares values through equality; is compares object identity. Use == for IDs, '
            'names, and values; use is/is not for singletons such as None, never to compare '
            'ordinary strings or numbers.',
  'learn_intent': 'Use equality for values and identity only for sentinels.',
  'base_concepts': ['==', 'is', 'object identity', 'None', 'equality methods'],
  'topic_deepdive': '<p>== asks whether values are equal; is asks whether two references point at '
                    'the same object.</p><p>Use `is None` for absence, but compare patient IDs, '
                    'strings, and numeric values with ==.</p>',
  'interview_qa': [{'q': 'Why not use is for strings?',
                    'a': 'Interning and allocation make identity incidental.'},
                   {'q': 'Can == run custom code?',
                    'a': "Yes; it can call an object's __eq__ method."}],
  'subsection': '',
  'prompt_full': "What's the difference between == and is operators? In a healthcare system, when "
                 'would you use each to compare patient data?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R5',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'Dynamic-array performance',
  'question': 'How does the underlying data structure of Python lists (dynamic arrays) affect '
              'performance when inserting patient records at different positions? Compare with '
              "tuple's immutable structure.",
  'answer': 'List append is amortized O(1), while front/middle insertion is O(n) due to shifts. A '
            'tuple cannot be edited: creating a modified tuple copies elements, so select a deque '
            'or list based on mutation pattern.',
  'learn_intent': 'Reinforce dynamic-array shifts and tuple immutability trade-offs.',
  'base_concepts': ['list append', 'list insertion', 'tuple immutability', 'Big O', 'deque'],
  'topic_deepdive': '<p>Front insertion in a list shifts existing references, while append usually '
                    'uses spare capacity.</p><p>Tuples cannot be changed in place; creating a '
                    'modified tuple creates a new object.</p>',
  'interview_qa': [{'q': 'What is pop(0) complexity?', 'a': 'O(n) for a list.'},
                   {'q': 'What queue supports O(1) ends?', 'a': 'collections.deque.'}],
  'subsection': '',
  'prompt_full': 'How does the underlying data structure of Python lists (dynamic arrays) affect '
                 'performance when inserting patient records at different positions? Compare with '
                 "tuple's immutable structure.",
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R6',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'Empty collection overhead',
  'question': "What's the memory overhead difference between an empty list [] and empty tuple ()? "
              'Why does this matter when handling large healthcare datasets?',
  'answer': 'An empty tuple is smaller because it is fixed-size and may be shared as a singleton '
            'in CPython; a list reserves mutable-container state. Measure on the target '
            'interpreter, but multiply small per-record overhead by millions before choosing a '
            'representation.',
  'learn_intent': 'Consider per-object overhead when representing very large datasets.',
  'base_concepts': ['memory overhead', 'empty tuple', 'empty list', 'sys.getsizeof', 'allocation'],
  'topic_deepdive': '<p>Tuples have less mutable-container overhead than lists; CPython may also '
                    'share the empty tuple singleton.</p><p>Measure with sys.getsizeof on the '
                    'deployment interpreter because implementation details vary.</p>',
  'interview_qa': [{'q': 'Does getsizeof include nested objects?',
                    'a': 'No; it reports the shallow object size.'},
                   {'q': 'Why does tiny overhead matter?',
                    'a': 'Millions of records multiply it into material memory use.'}],
  'subsection': '',
  'prompt_full': "What's the memory overhead difference between an empty list [] and empty tuple "
                 '()? Why does this matter when handling large healthcare datasets?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R7',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'Garbage collection cycles',
  'question': "How does Python's garbage collection work with circular references? Give an example "
              'with patient-doctor relationships in a hospital management system.',
  'answer': 'Reference counting releases most objects immediately; cyclic GC finds unreachable '
            'reference cycles. A Patient referring to Doctor and Doctor referring back forms a '
            'cycle; avoid unnecessary back references or use weakref when the relationship should '
            'not own the object.',
  'learn_intent': 'Explain reference counting and cyclic garbage collection accurately.',
  'base_concepts': ['reference counting',
                    'cyclic GC',
                    'circular references',
                    'weakref',
                    'object lifetime'],
  'topic_deepdive': '<p>CPython usually frees objects when reference counts reach zero. Cyclic GC '
                    'additionally finds unreachable groups that reference each other.</p><p>A '
                    'Patient-to-Doctor and Doctor-to-Patient cycle may need weak references if one '
                    'link should not own the other.</p>',
  'interview_qa': [{'q': 'Why is reference counting insufficient alone?',
                    'a': 'A cycle can keep every count above zero.'},
                   {'q': 'What is weakref for?',
                    'a': 'Referencing an object without extending its lifetime.'}],
  'subsection': '',
  'prompt_full': "How does Python's garbage collection work with circular references? Give an "
                 'example with patient-doctor relationships in a hospital management system.',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R8',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'Generator review',
  'question': 'Explain how generator expressions maintain state between iterations. Why would you '
              'choose generators over list comprehensions when processing millions of patient '
              'records?',
  'answer': 'The generator frame preserves locals and the next instruction between yields. It '
            'evaluates lazily, reducing peak memory and enabling pipelines, but results are '
            'consumed once.',
  'learn_intent': 'Reinforce lazy generator execution for large record streams.',
  'base_concepts': ['generator expression',
                    'lazy evaluation',
                    'iteration state',
                    'memory use',
                    'exhaustion'],
  'topic_deepdive': '<p>Each next call resumes the generator where it paused, retaining only its '
                    'frame and current locals.</p><p>This supports streaming batches of patient '
                    'records without allocating a full transformed list.</p>',
  'interview_qa': [{'q': 'When does a generator raise a data error?',
                    'a': 'Usually when iteration reaches the bad item.'},
                   {'q': 'What consumes a generator?',
                    'a': 'list(), sum(), a loop, or another iterator consumer.'}],
  'subsection': '',
  'prompt_full': 'Explain how generator expressions maintain state between iterations. Why would '
                 'you choose generators over list comprehensions when processing millions of '
                 'patient records?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R9',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'LEGB review',
  'question': "How does Python's name resolution work with the LEGB rule? Provide an example with "
              'nested functions in a medical diagnosis system.',
  'answer': 'A nested rule function first sees its locals, then enclosing diagnosis context, '
            'module globals, and builtins. Pass clinical configuration explicitly when possible; '
            'use nonlocal only to rebind an enclosing value.',
  'learn_intent': 'Trace LEGB lookups in nested diagnostic-rule functions.',
  'base_concepts': ['LEGB', 'nested functions', 'closures', 'shadowing', 'nonlocal'],
  'topic_deepdive': '<p>A nested rule can see an enclosing patient context unless it defines a '
                    'local name that shadows it.</p><p>Explicit parameters are often easier to '
                    'test than relying on distant globals for clinical thresholds.</p>',
  'interview_qa': [{'q': 'What is shadowing?',
                    'a': 'A nearer scope binding hides a name in an outer scope.'},
                   {'q': 'How can a nested function change an enclosing value?',
                    'a': 'Declare that name nonlocal.'}],
  'subsection': '',
  'prompt_full': "How does Python's name resolution work with the LEGB rule? Provide an example "
                 'with nested functions in a medical diagnosis system.',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'R10',
  'section': 'Reasoning Bank',
  'kind': 'reasoning',
  'title': 'Missing blood type access',
  'question': "What happens internally when you use patient_data.get('blood_type') vs "
              "patient_data['blood_type']? When is each approach appropriate in healthcare "
              'applications?',
  'answer': 'get performs a lookup and returns None/default on absence; subscription raises '
            'KeyError on absence. Use subscription for required validated data and get for '
            'genuinely optional data with an explicit missing-data workflow.',
  'learn_intent': 'Reinforce optional versus required dictionary access decisions.',
  'base_concepts': ['dict.get', 'subscription', 'KeyError', 'defaults', 'missing data'],
  'topic_deepdive': '<p>get performs the same lookup but converts absence into None or a supplied '
                    'default. Subscription signals a contract violation with KeyError.</p><p>For '
                    'blood type, distinguish unknown data from a legitimate value rather than '
                    'silently substituting text.</p>',
  'interview_qa': [{'q': "What does patient_data['blood_type'] do if missing?",
                    'a': 'Raises KeyError.'},
                   {'q': 'Can get hide a data-quality issue?',
                    'a': 'Yes, if its default is treated as verified information.'}],
  'subsection': '',
  'prompt_full': "What happens internally when you use patient_data.get('blood_type') vs "
                 "patient_data['blood_type']? When is each approach appropriate in healthcare "
                 'applications?',
  'code_stub': '',
  'expected_output': ''},
 {'id': 'Q8.1',
  'section': 'Advanced Integration',
  'kind': 'integration',
  'title': 'Patient management system',
  'question': 'Create a complete patient management class that demonstrates all learned concepts:',
  'answer': 'Store records behind a small API, validate at ingestion, capture vitals as immutable '
            'snapshots, and generate reports lazily. Keep business rules deterministic and '
            'separate educational data processing from real clinical decision making.',
  'learn_intent': 'Integrate data modeling, validation, flexible APIs, and lazy reporting in one '
                  'coherent class.',
  'base_concepts': ['class design',
                    'type hints',
                    '*args/**kwargs',
                    'generators',
                    'comprehensions',
                    'functional operations'],
  'topic_deepdive': '<p>A small management class should validate on entry, own its mutable record '
                    'state, and expose deliberate operations for vitals and '
                    'reports.</p><p>Generators make reports lazy, while batch operations should '
                    'return clear successes or errors without hiding partial failure.</p>',
  'interview_qa': [{'q': 'Why validate in add_patient?',
                    'a': 'It prevents malformed state from spreading through later methods.'},
                   {'q': 'Why store vitals as snapshots?',
                    'a': 'A captured reading should not change when a caller later mutates input '
                         'data.'}],
  'code_file': 'Q8_1_patient_system.py',
  'subsection': '',
  'prompt_full': 'Create a complete patient management class that demonstrates all learned '
                 'concepts:',
  'code_stub': 'class PatientManagementSystem:\n'
               '    """\n'
               '    Integrate all Python concepts in a comprehensive healthcare system:\n'
               '    - Use appropriate data types for different medical data\n'
               '    - Implement type hints throughout\n'
               '    - Use comprehensions for data processing\n'
               '    - Apply functional programming concepts\n'
               '    - Handle different types of medical operations\n'
               '    """\n'
               '    \n'
               '    def __init__(self):\n'
               '        # Initialize with appropriate data structures\n'
               '        pass\n'
               '    \n'
               '    def add_patient(self, **patient_data):\n'
               '        # Use **kwargs and type validation\n'
               '        pass\n'
               '    \n'
               '    def update_vitals(self, patient_id: str, *vitals, **metadata):\n'
               '        # Demonstrate *args and **kwargs usage\n'
               '        pass\n'
               '    \n'
               '    def generate_report(self, filter_func=lambda p: True):\n'
               '        # Use lambda functions and generators\n'
               '        pass\n'
               '    \n'
               '    def batch_process(self, operations: list):\n'
               '        # Use map, filter, reduce appropriately\n'
               '        pass',
  'expected_output': ''}]
