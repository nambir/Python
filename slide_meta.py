"""Definitions and interview explanation scripts for each slide."""

SLIDE_META = {
    2: {
        "definition": "Python is a high-level, interpreted programming language known for readable syntax. Setup means installing the Python runtime, an editor, and learning how to run .py files or use the REPL.",
        "interview": "Python is an interpreted, dynamically typed language — I don't declare types upfront. I write code in .py files and run them with python filename.py, or test quickly in the REPL. Coming from C#, the biggest shift is no braces or semicolons — indentation defines blocks.",
    },
    3: {
        "definition": "A Python program is a script executed line by line. print() sends output to the console. The if __name__ == '__main__' guard runs code only when the file is executed directly, not when imported.",
        "interview": "print() is Python's Console.WriteLine. Every .py file runs top to bottom. I use if __name__ == '__main__' as the entry point — it only runs when I execute the file directly, similar to a Main method but optional and idiomatic for reusable modules.",
    },
    4: {
        "definition": "Variables are names bound to objects in memory. Python is dynamically typed — you assign values without declaring types, but types exist at runtime and can be checked with type().",
        "interview": "In Python I just write x = 10 — no int keyword. Python is dynamically typed, meaning the type is determined at runtime, but strongly typed, meaning it won't silently convert incompatible types like string plus integer. I can check types with type() when needed.",
    },
    5: {
        "definition": "A string is an immutable sequence of Unicode characters. Python supports slicing, formatting (especially f-strings), and built-in methods like upper(), split(), and replace().",
        "interview": "Strings are immutable in Python — once created they can't be changed, only new strings are made. I use f-strings for formatting, like f'Hello {name}', which is similar to C# interpolated strings. Slicing like text[0:3] or text[-1] is a common interview topic.",
    },
    6: {
        "definition": "Python supports integers, floats, and complex numbers. Key operators include / for true division, // for floor division, % for modulo, and ** for exponentiation.",
        "interview": "Unlike C#, Python's / always returns a float — 17/5 is 3.4. For integer division I use //. Modulo % gives the remainder, and ** is power. divmod(a,b) returns both quotient and remainder in one call.",
    },
    7: {
        "definition": "bool represents True or False. None is the singleton representing absence of a value (like null). Python uses truthiness — empty or zero values evaluate to False in conditionals.",
        "interview": "None is Python's null — I always check with 'is None', not == None, because is checks identity. Truthiness is important: empty string, zero, empty list are all falsy. A common trap is bool('False') returns True because any non-empty string is truthy.",
    },
    8: {
        "definition": "Conditional statements (if, elif, else) execute blocks based on boolean expressions. Python uses a colon and indentation instead of braces to define blocks.",
        "interview": "Python conditionals work like C# if/else but without parentheses required and with elif instead of else if. The block is defined by indentation, typically 4 spaces. I can also write a one-line ternary: result = 'pass' if score >= 60 else 'fail'.",
    },
    9: {
        "definition": "A for loop iterates over any iterable (list, string, range, etc.). range() generates number sequences. enumerate() provides both index and value during iteration.",
        "interview": "Python's for loop is like C# foreach — I write for item in collection, not for(int i=0...). When I need indexes I use enumerate(). range(5) gives 0 through 4, and range(1,6) gives 1 through 5.",
    },
    10: {
        "definition": "A while loop repeats while a condition is true. break exits the loop early; continue skips to the next iteration. Python uniquely allows an else clause on loops that runs if no break occurred.",
        "interview": "while works the same conceptually as C#. break stops the loop, continue skips the rest of the current iteration. One Python-specific detail: a for/while else block runs only if the loop completed without hitting break — useful for search patterns.",
    },
    11: {
        "definition": "A list is a mutable, ordered collection that can hold mixed types. It supports indexing, slicing, and methods like append(), insert(), pop(), sort(), and reverse().",
        "interview": "Lists are Python's most used collection — like a C# List but untyped and more flexible. They're mutable and ordered. Slicing like nums[1:3] returns a new sublist. nums[::-1] reverses without modifying the original. append is amortized O(1).",
    },
    12: {
        "definition": "A tuple is an immutable ordered collection, often used for fixed data. A set is an unordered collection of unique elements supporting mathematical operations like union and intersection.",
        "interview": "I use tuples when data shouldn't change — they're immutable and can be dictionary keys. Sets automatically remove duplicates and are great for membership tests in O(1). For example, set([1,2,2,3]) gives {1,2,3}.",
    },
    13: {
        "definition": "A dictionary stores key-value pairs with fast O(1) lookup. Keys must be hashable (immutable types). dict.get(key, default) safely returns a fallback for missing keys.",
        "interview": "Dictionaries are like C# Dictionary — key-value pairs with fast lookup. I prefer .get('key', default) over direct access to avoid KeyError. Dict comprehensions like {n: n*n for n in range(5)} are idiomatic and often asked in interviews.",
    },
    14: {
        "definition": "Functions are reusable blocks defined with def. They support default parameters, *args for variable positional arguments, and **kwargs for variable keyword arguments. Functions are first-class objects.",
        "interview": "I define functions with def name(params): and return sends a value back. *args collects extra positional args as a tuple, **kwargs collects keyword args as a dict. The classic trap is mutable default arguments — def f(lst=[]) shares the same list across calls; I use None instead.",
    },
    15: {
        "definition": "lambda creates small anonymous functions. map() transforms each element; filter() keeps elements matching a condition. These enable functional-style programming.",
        "interview": "lambda is a one-line anonymous function — like x: x*2. map applies a function to every item, filter keeps items where the function returns True. In practice I often prefer list comprehensions, but I should know lambda for sorting: sorted(items, key=lambda x: x[1]).",
    },
    16: {
        "definition": "Comprehensions provide a concise syntax to build lists, sets, or dictionaries from iterables with optional filtering — a Pythonic alternative to loops or map/filter.",
        "interview": "Comprehensions are the Pythonic way to build collections. [x*2 for x in nums if x%2==0] replaces a for loop plus append. They're more readable than map/filter and show you write idiomatic Python — interviewers love seeing them.",
    },
    17: {
        "definition": "OOP (Object-Oriented Programming) organizes code around objects with four pillars: Encapsulation, Inheritance, Polymorphism, and Abstraction. Python supports all four — with conventions slightly different from C#.",
        "interview": "Python is fully object-oriented — even numbers and functions are objects. The four pillars are encapsulation with _private convention, inheritance via class Child(Parent), polymorphism by overriding methods or duck typing, and abstraction using ABC abstract classes or informal interfaces.",
    },
    18: {
        "definition": "A class is a blueprint; an object is an instance. Encapsulation bundles data and methods together and hides internals using the _underscore convention and @property.",
        "interview": "I define a class with __init__ as constructor and self as the first parameter like C# this. For encapsulation I prefix internal fields with underscore — Python has no private keyword. @property gives controlled read access like a C# property getter.",
    },
    19: {
        "definition": "Inheritance reuses parent class code via class Child(Parent). Polymorphism lets the same method call behave differently — through overriding or duck typing (if it has the method, it works).",
        "interview": "I inherit with class Dog(Animal) and call super().__init__() like base constructor in C#. Polymorphism: I override speak() in Dog and Cat, loop a list of animals, each returns different sound. Duck typing means I don't need a formal interface — if it has the method, it works.",
    },
    20: {
        "definition": "Abstraction hides complex implementation behind a simple interface — using ABC + @abstractmethod (like C# abstract class) or duck typing. Magic methods (__str__, __eq__) customize object behavior.",
        "interview": "For abstraction I use ABC from abc module with @abstractmethod — like C# abstract class. Duck typing is Python's informal alternative to interfaces. __str__ is for users like ToString(), __repr__ for debugging, __eq__ for Equals().",
    },
    21: {
        "definition": "A module is any .py file. import loads a module; from...import brings specific names. __name__ is '__main__' when run directly, otherwise the module name — enabling reusable code.",
        "interview": "Every .py file is a module. import math loads the whole module; from math import sqrt imports one function. The __name__ variable tells me if the file is run directly or imported — that's how I guard my test/entry code.",
    },
    22: {
        "definition": "File I/O reads and writes data to the filesystem. The with statement (context manager) automatically closes files. Modes: 'r' read, 'w' write, 'a' append.",
        "interview": "I always use with open('file.txt', 'r', encoding='utf-8') as f — it auto-closes the file, like C# using statement. I specify encoding explicitly for text files. I can read line by line with for line in f, which is memory-efficient for large files.",
    },
    23: {
        "definition": "Exception handling uses try/except/finally to catch and handle runtime errors. raise throws exceptions. Custom exceptions inherit from Exception.",
        "interview": "try/except is like try/catch in C#. I catch specific exceptions like ValueError, not bare except, because that catches everything including KeyboardInterrupt. finally always runs for cleanup. I raise exceptions to signal invalid input to callers.",
    },
    24: {
        "definition": "Python's standard library provides built-in modules for common tasks: os for filesystem, json for serialization, datetime for dates, sys for interpreter settings.",
        "interview": "Python has batteries included. I use os.getcwd() for paths, json.dumps/loads for API data — like System.Text.Json in C#. datetime handles dates; timedelta adds or subtracts days. I don't need to install these — they ship with Python.",
    },
    25: {
        "definition": "Common coding interview patterns in Python include string reversal, frequency counting with dicts, FizzBuzz, palindrome checks, and hash-map techniques like two-sum.",
        "interview": "For two-sum I use a hash map — store each number's index, check if target minus current exists in O(n). For frequency counting I use dict.get(ch, 0) + 1 or collections.Counter. I always state time and space complexity — dict lookups are O(1) average.",
    },
    26: {
        "definition": "Core Python interview topics include data type differences, identity vs equality, mutability traps, the GIL, args/kwargs, and Python-specific behaviors like truthiness and context managers.",
        "interview": "I structure oral answers as: definition, example, when to use it. For list vs tuple: list is mutable for changing data, tuple is immutable for fixed records. For == vs is: == compares values, is compares memory identity — I use is only for None, True, False.",
    },
    27: {
        "definition": "HTTP is the protocol for web communication. REST is an architectural style using HTTP methods (GET, POST, PUT, DELETE) on resources identified by URLs, typically exchanging JSON data.",
        "interview": "REST APIs use HTTP verbs on resource URLs — GET reads, POST creates, PUT updates, DELETE removes. I return proper status codes: 200 success, 201 created, 404 not found, 400 bad request. JSON is the standard body format. In Python I use the requests library to call APIs.",
    },
    28: {
        "definition": "FastAPI is a modern Python web framework for building APIs. It uses Python type hints for validation and automatically generates OpenAPI/Swagger documentation.",
        "interview": "FastAPI is like ASP.NET Web API — I define routes with decorators like @app.get('/users/{id}'). It auto-validates inputs from type hints and returns JSON from dictionaries. Swagger docs are free at /docs. It's fast and ideal for microservices and interview demos.",
    },
    29: {
        "definition": "POST endpoints accept data in the request body. Pydantic models define and validate the shape of request/response data, similar to DTOs with data annotations in C#.",
        "interview": "For POST I define a Pydantic BaseModel — like a C# DTO with validation attributes. FastAPI reads the JSON body, validates it, and returns 422 if invalid. This gives me type-safe APIs with minimal boilerplate — the model doubles as documentation.",
    },
    30: {
        "definition": "CRUD means Create, Read, Update, Delete — the four basic database/API operations mapped to POST, GET, PUT/PATCH, and DELETE HTTP methods on a resource.",
        "interview": "I design CRUD with noun-based URLs: POST /todos creates, GET /todos lists, PUT /todos/{id} updates, DELETE /todos/{id} removes. I return 201 on create with the new resource, 404 when ID not found via HTTPException. I test everything in Swagger UI.",
    },
    31: {
        "definition": "API interview topics cover REST principles, HTTP status codes, authentication basics, idempotency, pagination, and API design patterns like versioning and error handling.",
        "interview": "GET, PUT, DELETE are idempotent — calling twice has the same effect. POST is not — each call may create a new resource. 401 means not logged in, 403 means logged in but forbidden. For pagination I'd add ?page=1&limit=20 query params and return total count in the response.",
    },
    32: {
        "definition": "Python offers multiple UI approaches: Streamlit for quick web dashboards, Tkinter for desktop apps, Flask/Django for full web apps, and FastAPI for API backends paired with any frontend.",
        "interview": "For quick prototypes I use Streamlit — pure Python, no HTML needed. For desktop, Tkinter is built in. For production web apps, Flask or Django. I pair FastAPI backend with Streamlit or React frontend — same separation as .NET Web API plus Blazor or Angular.",
    },
    33: {
        "definition": "Streamlit is a Python library that turns scripts into interactive web apps. Widgets like buttons, text inputs, and sliders are created with simple function calls.",
        "interview": "Streamlit lets me build a UI in pure Python — st.title, st.text_input, st.button. When a user interacts, the script reruns top to bottom. It's perfect for data dashboards and quick demos. I run it with streamlit run app.py and it opens in the browser.",
    },
    34: {
        "definition": "A client UI can consume a REST API using HTTP requests. Separating frontend (Streamlit) from backend (FastAPI) follows the same architecture as modern web applications.",
        "interview": "I keep UI and API separate — Streamlit calls FastAPI with requests.get/post. This decoupled architecture means I can swap the UI or API independently. Same pattern as Angular calling a .NET API. I handle connection errors gracefully when the API isn't running.",
    },
    35: {
        "definition": "Tkinter is Python's built-in GUI toolkit. It provides windows, buttons, labels, and text fields with an event-driven model centered on mainloop().",
        "interview": "Tkinter is Python's standard desktop UI — like WinForms. I create a root window, add widgets with pack() or grid(), and bind button commands to functions. root.mainloop() starts the event loop waiting for clicks. It's built into Python on Windows — no extra install.",
    },
    36: {
        "definition": "A full-stack Python project combines a FastAPI backend (business logic, data) with a Streamlit frontend (user interface), communicating over HTTP REST calls.",
        "interview": "My capstone runs two services: FastAPI on port 8001 handles CRUD logic, Streamlit UI calls it via HTTP. This shows I understand separation of concerns, REST integration, and end-to-end delivery. I'd demo it live: add a todo, toggle it, delete it — and explain the request flow.",
    },
    37: {
        "definition": "Real project structure organizes Python code into folders by responsibility — routes, services, schemas, models, tests, and config — so teams can scale, test, and deploy professionally.",
        "interview": "A real Python API project separates concerns: routes handle HTTP, services hold business logic, schemas validate data, models map to the database, and tests mirror the app in a tests/ folder. This is like a C# solution with Controllers, Services, DTOs, and Entities in separate folders.",
    },
    38: {
        "definition": "A learning project uses numbered single-file scripts (03_hello_world.py) or small demo folders — optimized for practice, not production deployment.",
        "interview": "During learning I use one file per topic for quick practice. In production I'd never put everything in one file — I'd use packages and layers. I can point to my Projects/ folder as learning work and describe how I'd restructure it for a real job.",
    },
    39: {
        "definition": "A production FastAPI project typically has app/main.py as entry point, api/routes for endpoints, schemas for Pydantic DTOs, services for business logic, models for database entities, core for config, and tests/ for pytest.",
        "interview": "I structure FastAPI as: main.py creates the app and includes routers. Routes are thin — they call services. Services contain business rules. Schemas define request/response shapes. Models are database tables. Config lives in core/ and reads from .env. Tests live outside app/ in tests/.",
    },
    40: {
        "definition": "A full-stack monorepo keeps backend/, frontend/, docs/, and scripts/ in one git repository when multiple deployable services belong to the same product.",
        "interview": "In a monorepo I'd have backend/ for FastAPI, frontend/ for Streamlit or React, shared/ for common code, and docs/ for architecture. The UI calls the API over HTTP — same pattern as Angular plus .NET API. docker-compose.yml can run both services locally.",
    },
    41: {
        "definition": "Creating a real project means scaffolding root config files (requirements.txt, .env.example, README), an app/ package with layered subfolders, and tests/ — then implementing one feature end-to-end through all layers.",
        "interview": "I start with mkdir, requirements.txt, and app/main.py. Then I add routes, schemas, and services one feature at a time. I never commit .env with secrets. I document run commands in README. I can walk an interviewer through the tree top-down in under two minutes.",
    },
    42: {
        "definition": "Python-Set2 is a portfolio of six real project areas — pythonBasics, google-python-exercises, pandas, Django, Django REST, and Pipecat voice AI — each mapping to topics in this deck.",
        "interview": "I keep a structured portfolio in Python-Set2: fundamentals in pythonBasics/, classic exercises for regex and files, pandas notebooks for data, Django and DRF for full-stack REST, and Pipecat POCs for voice AI. I can point an interviewer to the exact folder for any topic they ask about.",
    },
    43: {
        "definition": "pythonBasics/ contains seven topic modules (MyClass, MyCollections, MyLoops, MyModules, MyExceptionHandling, MyDebug, MyUnitTesting) — each a runnable mini-project reinforcing core Python skills.",
        "interview": "For OOP I open MyClass/ and walk through classes, self, and inheritance. For collections I use MyCollections/. For testing I show MyUnitTesting/ with pytest. Each folder is a focused module — it proves I didn't just read slides, I wrote and ran real code.",
    },
    44: {
        "definition": "google-python-exercises/ teaches file I/O, regex, and OS operations through classic puzzles. pandas/ uses Jupyter notebooks to analyze Titanic and FIFA CSV datasets with DataFrames, groupby, and filtering.",
        "interview": "google-python-exercises/babynames/ is great for regex interviews — I parse files and count patterns. For data roles I open my Titanic notebook and explain read_csv, filtering, groupby, and handling missing values. pandas is like LINQ on in-memory tables.",
    },
    45: {
        "definition": "djangobasics/meeting_planner/ is a Django 4 app with models, templates, auth, and a JWT API. DjangoRestBasics/inventory/ is a multi-app DRF project with serializers and ViewSets for drink, merchant, and supplier resources.",
        "interview": "Django gives me ORM, admin, auth, and templates out of the box — meeting_planner/ shows MVT plus a JWT API. DRF inventory/ shows serializers and ViewSets — similar to FastAPI routers plus Pydantic, but Django-native. I compare both when asked about Python web frameworks.",
    },
    46: {
        "definition": "Pipecat-Project/ contains voice AI POCs: pipecat-quickstart (cloud), phase1 (local services), phase2 (full pipeline), and voice-bouncer (IVR-style auth). Pipecat orchestrates STT → LLM → TTS over WebRTC.",
        "interview": "I built voice pipelines in phases — first local STT/LLM/TTS, then the full Pipecat framework. voice-bouncer/ demos an IVR flow with step-by-step processors. It's the same layered architecture as a REST API, but streaming audio instead of JSON — FastAPI backend plus Pipecat processors plus WebRTC client.",
    },
    47: {
        "definition": "A structured learning path through Python-Set2: week 1 basics, week 2 OOP/tests, week 3 pandas, week 4 web APIs, week 5 voice AI — with interview talking points for each area.",
        "interview": "I studied Python-Set2 in order: pythonBasics for fundamentals, google exercises for regex, pandas for data, Django and DRF for REST, Pipecat for voice AI. In interviews I demo 2–3 projects deeply rather than listing everything — and I always connect each project back to the concept they're asking about.",
    },
    48: {
        "definition": "A quick reference mapping C# concepts to Python equivalents, covering syntax, collections, OOP, web development, and error handling — essential for developers transitioning between languages.",
        "interview": "Coming from C#, I highlight key differences: no type declarations, indentation over braces, duck typing over interfaces, and Python's unified list type vs C# generics. I also note similarities: both are strongly typed, object-oriented, and have rich ecosystems for web and API development.",
    },
}
