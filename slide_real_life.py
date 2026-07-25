"""Real-life workplace examples for every slide — indented code blocks."""

REAL_LIFE: dict[int, str] = {
    1: (
        "<b>Order automation bot:</b> A logistics team runs a nightly sync — "
        "no Visual Studio build; CPython executes the <code>.py</code> directly."
        '<div class="step-pre">'
        "def sync_orders():\n"
        "    orders = fetch_from_api()\n"
        "    for order in orders:\n"
        "        if order.status == \"NEW\":\n"
        "            save_to_db(order)\n"
        "        else:\n"
        "            skip(order)\n"
        "\n"
        'if __name__ == "__main__":\n'
        "    sync_orders()"
        "</div>"
    ),
    2: (
        "<b>New laptop day-1:</b> Install Python, verify tools, then run the setup check."
        '<div class="step-pre">'
        "# PowerShell / terminal\n"
        "python --version\n"
        "pip --version\n"
        "\n"
        "# Then in Cursor: Select Interpreter → Python 3.12\n"
        "python Projects/00_windows_setup.py"
        "</div>"
    ),
    3: (
        "<b>Training week plan:</b> Same flow a team uses — docs → kata → real repo."
        '<div class="step-pre">'
        "# 1) Theory\n"
        "#    open PythonTraining.html\n"
        "# 2) Short practice\n"
        "python Projects/01_datatypes.py\n"
        "# 3) Deeper practice\n"
        "python Python-Set2/pythonBasics/MyCollections/mylist.py"
        "</div>"
    ),
    4: (
        "<b>PR review gate:</b> CI enforces PEP 8 / docstrings before merge."
        '<div class="step-pre">'
        "def calc_gst(amount):\n"
        '    """Return 18% GST for the given amount."""\n'
        "    return amount * 0.18\n"
        "\n"
        "# CI commands (PEP 8 + packaging)\n"
        "ruff check .\n"
        "# versions live in pyproject.toml (PEP 621)"
        "</div>"
    ),
    5: (
        "<b>E-commerce checkout:</b> List grows; GPS pin is a fixed tuple; order can mix types."
        '<div class="step-pre">'
        'cart = [\n'
        '    {"sku": "A1", "qty": 2},\n'
        '    {"sku": "B2", "qty": 1},\n'
        "]\n"
        "cart.append({\"sku\": \"C3\", \"qty\": 3})  # list grows\n"
        "\n"
        "delivery_pin = (12.97, 80.22)  # fixed GPS — tuple\n"
        'order = [101, "SHIPPED", ["Google", "Amazon"]]  # heterogeneous'
        "</div>"
    ),
    6: (
        "<b>Payment API contract:</b> Type hints + mypy catch bad calls before production."
        '<div class="step-pre">'
        "from decimal import Decimal\n"
        "\n"
        "def charge(amount: Decimal, currency: str) -> str:\n"
        "    return f\"Charged {amount} {currency}\"\n"
        "\n"
        '# Bad call (wrong types):\n'
        'result = charge("100", 91)\n'
        "print(result)"
        "</div>"
        '<table class="data-tbl">'
        "<tr><th>Case</th><th>Input (what you type)</th><th>Output (what you see)</th></tr>"
        "<tr>"
        "<td><b>Without mypy</b></td>"
        "<td><code>python app.py</code></td>"
        "<td>Hints ignored — program <b>runs</b>. Example print:<br>"
        "<code>Charged 100 91</code><br>"
        "(no type error from Python itself)</td>"
        "</tr>"
        "<tr>"
        "<td><b>With mypy</b></td>"
        "<td><code>mypy app.py</code></td>"
        "<td>Type errors reported — program is <b>not</b> executed. Example:<br>"
        "<code>error: Argument 1 … expected \"Decimal\"</code><br>"
        "<code>error: Argument 2 … expected \"str\"</code><br>"
        "<code>Found 2 errors in 1 file</code></td>"
        "</tr>"
        "<tr>"
        "<td><b>Correct call</b></td>"
        "<td><code>charge(Decimal(\"100.00\"), \"INR\")</code><br>"
        "then <code>python app.py</code></td>"
        "<td><code>Charged 100.00 INR</code> — OK for mypy and Python</td>"
        "</tr>"
        "</table>"
        '<p class="step-result">'
        "<b>Remember:</b> mypy does <b>not</b> run automatically with Python. "
        "You run it separately (or in CI)."
        "</p>"
    ),
    7: (
        "<b>Invoice math:</b> Arithmetic, floor division, identity, membership, walrus."
        '<div class="step-pre">'
        "qty = 3\n"
        "price = 250\n"
        "total = qty * price          # 750\n"
        "pages = 25 // 10             # floor division → 2\n"
        "\n"
        "status = None\n"
        "if status is None:           # empty?\n"
        '    print("pending")\n'
        "\n"
        'customer = "Ravi"\n'
        "if customer is not None:     # has a value?\n"
        '    print("bill to", customer)\n'
        "\n"
        'tax_codes = ["GST", "CGST"]\n'
        'if "GST" in tax_codes:\n'
        '    print("apply GST")\n'
        "\n"
        "# ── Walrus :=  (Python 3.8+) ──\n"
        "# Assign AND use the value in one expression\n"
        'lines = ["a", "b", "c"]\n'
        "\n"
        "# Without walrus (two steps):\n"
        "n = len(lines)\n"
        "if n > 0:\n"
        "    print(n)                 # 3\n"
        "\n"
        "# With walrus (one expression):\n"
        "if (n := len(lines)) > 0:\n"
        "    print(n)                 # 3 — same result, shorter\n"
        "\n"
        "# Real invoice use: count items while checking\n"
        "items = [\"Pen\", \"Notebook\", \"Bag\"]\n"
        "if (count := len(items)) >= 3:\n"
        '    print(f"Bulk order: {count} lines")'
        "</div>"
        '<p class="step-result">'
        "<b>None:</b> <code>is None</code> = empty; <code>is not None</code> = has a value.<br>"
        "<b>Walrus <code>:=</code>:</b> assign inside <code>if</code>/<code>while</code> so you do not call "
        "<code>len()</code> (or <code>input()</code>) twice. Use when the value is needed in the condition "
        "<b>and</b> in the body. Do not use for every assignment — normal <code>=</code> is clearer then."
        "</p>"
    ),
    8: (
        "<b>CSV import job:</b> Branch, skip bad rows, stop early, stub unfinished work."
        '<div class="step-pre">'
        "for i, row in enumerate(reader):\n"
        "    if not row.get(\"id\"):\n"
        "        continue              # skip bad row\n"
        "    if i >= 10000:\n"
        "        break                 # stop after 10,000\n"
        '    if row["country"] == "IN":\n'
        "        apply_in_tax(row)\n"
        '    elif row["country"] == "US":\n'
        "        apply_us_tax(row)\n"
        "    else:\n"
        "        apply_default_tax(row)\n"
        "\n"
        "def apply_coupon():\n"
        "    pass                      # stub — fill later"
        "</div>"
    ),
    9: (
        "<b>Salary sheet transform:</b> Comprehension vs loop; generator for huge files."
        '<div class="step-pre">'
        "# Instead of a 10-line loop:\n"
        "net = []\n"
        "for g, tax in zip(gross, taxes):\n"
        "    if g > 0:\n"
        "        net.append(g - tax)\n"
        "\n"
        "# Same result — one list comprehension:\n"
        "net = [g - tax for g, tax in zip(gross, taxes) if g > 0]\n"
        "\n"
        "# --- Huge file + generator (why?) ---\n"
        "# Huge file  = millions of lines (too big to load all at once into a list).\n"
        "# Generator  = give me ONE parsed line at a time (yield), not a giant list.\n"
        "# Lazy      = work happens only when you ask for the next line → less RAM.\n"
        "\n"
        "# WITHOUT yield — builds a FULL list in memory (risky for huge files):\n"
        "def parse_lines_list(f):\n"
        "    results = []\n"
        "    for line in f:\n"
        "        results.append(parse(line))\n"
        "    return results              # everything ready at once\n"
        "\n"
        "# WITH yield — same loop, but one value at a time (safe):\n"
        "def parse_lines(f):              # f = open text file\n"
        "    for line in f:               # read one line from disk\n"
        "        yield parse(line)        # hand back ONE result; pause; wait for next ask\n"
        "\n"
        "# Use the generator like:\n"
        "# for row in parse_lines(open('huge.csv')):\n"
        "#     process(row)              # only one row lives in memory at a time"
        "</div>"
        '<p class="step-result"><b>Rule:</b> if the function body uses <b>yield</b> → it is a <b>GENERATOR</b> function.</p>'
    ),
    10: (
        "<b>Invoice tax helper:</b> Pure function + higher-order use in a report."
        '<div class="step-pre">'
        "def calc_gst(amount):\n"
        "    return amount * 0.18      # pure: same in → same out\n"
        "\n"
        "def build_report(amounts, tax_fn):\n"
        "    rows = []\n"
        "    for amount in amounts:\n"
        "        rows.append({\n"
        '            "amount": amount,\n'
        '            "gst": tax_fn(amount),\n'
        "        })\n"
        "    return rows\n"
        "\n"
        "report = build_report([100, 200], calc_gst)"
        "</div>"
    ),
    11: (
        "<b>Report pipeline:</b> Clean lines, drop empties, find max sale, zip headers."
        '<div class="step-pre">'
        "lines = [\"  A  \", \"\", \"  B  \"]\n"
        "cleaned = list(map(str.strip, lines))\n"
        "cells = list(filter(None, cleaned))   # drop empty\n"
        "\n"
        "sales = [\n"
        '    {"item": "Laptop", "amount": 50000},\n'
        '    {"item": "Mouse", "amount": 800},\n'
        "]\n"
        "top = max(sales, key=lambda r: r[\"amount\"])\n"
        "\n"
        'headers = ["name", "qty"]\n'
        'row = ["Pen", "12"]\n'
        "record = dict(zip(headers, row))"
        "</div>"
    ),
    12: (
        "<b>Support dashboard:</b> Count statuses, group by assignee, chat buffer, light record."
        '<div class="step-pre">'
        "from collections import Counter, defaultdict, deque, namedtuple\n"
        "\n"
        'statuses = ["open", "open", "closed", "open"]\n'
        "pie = Counter(statuses)          # open: 3, closed: 1\n"
        "\n"
        "by_assignee = defaultdict(list)\n"
        'by_assignee["Ravi"].append(101)\n'
        'by_assignee["Anu"].append(102)\n'
        "\n"
        "chat = deque(maxlen=100)\n"
        'chat.append("hi")\n'
        "\n"
        'Ticket = namedtuple("Ticket", "id status")\n'
        't = Ticket(101, "open")'
        "</div>"
    ),
    13: (
        "<b>Overnight batch:</b> Global cache grows forever — fix with cleanup / weakref / with."
        '<div class="step-pre">'
        "# Problem: cache never clears\n"
        "cache = {}\n"
        "\n"
        "def process(order_id, huge_json):\n"
        "    cache[order_id] = huge_json   # memory climbs\n"
        "\n"
        "# Better: clear or use with for files\n"
        "def export_orders(path):\n"
        "    with open(path, encoding=\"utf-8\") as f:\n"
        "        for line in f:\n"
        "            yield line\n"
        "    # file closed here — don't wait for GC"
        "</div>"
    ),
    14: (
        "<b>Create-user API:</b> Pydantic coerces and validates — no hand-written if-checks."
        '<div class="step-pre">'
        "from pydantic import BaseModel, Field, field_validator\n"
        "\n"
        "class UserCreate(BaseModel):\n"
        "    email: str\n"
        "    age: int = Field(ge=18)\n"
        "\n"
        "    @field_validator(\"email\")\n"
        "    @classmethod\n"
        "    def lower_email(cls, v):\n"
        "        return v.lower()\n"
        "\n"
        'body = {"email": "Anu@Co.COM", "age": "25"}\n'
        "user = UserCreate.model_validate(body)\n"
        "# email → anu@co.com, age → 25; age &lt; 18 → 422"
        "</div>"
    ),
    15: (
        "<b>Bank / wallet domain:</b> Inheritance + polymorphism at month-end."
        '<div class="step-pre">'
        "class Account:\n"
        "    def __init__(self, balance):\n"
        "        self.balance = balance\n"
        "\n"
        "    def deposit(self, amount):\n"
        "        self.balance += amount\n"
        "\n"
        "    def withdraw(self, amount):\n"
        "        self.balance -= amount\n"
        "\n"
        "    def month_end(self):\n"
        "        pass\n"
        "\n"
        "class SavingsAccount(Account):\n"
        "    def month_end(self):\n"
        "        self.balance *= 1.04   # interest\n"
        "\n"
        "accounts = [Account(100), SavingsAccount(200)]\n"
        "for a in accounts:\n"
        "    a.month_end()            # polymorphism"
        "</div>"
    ),
    16: (
        "<b>ORM-style field:</b> Descriptor rejects negatives — like a C# property setter."
        '<div class="step-pre">'
        "class PositiveDecimal:\n"
        "    def __set_name__(self, owner, name):\n"
        "        self.name = name\n"
        "\n"
        "    def __get__(self, obj, owner):\n"
        "        return obj.__dict__.get(self.name)\n"
        "\n"
        "    def __set__(self, obj, value):\n"
        "        if value &lt; 0:\n"
        '            raise ValueError("price must be &gt;= 0")\n'
        "        obj.__dict__[self.name] = value\n"
        "\n"
        "class Product:\n"
        "    price = PositiveDecimal()\n"
        "\n"
        "p = Product()\n"
        "p.price = 99\n"
        "# p.price = -1  → ValueError"
        "</div>"
    ),
    17: (
        "<b>Export 50M+ CSV rows:</b> Stream with yield — avoid MemoryError from read().split()."
        '<div class="step-pre">'
        "def csv_reader(path):\n"
        "    with open(path, encoding=\"utf-8\") as f:\n"
        "        for line in f:\n"
        "            yield line.strip().split(\",\")\n"
        "\n"
        "def export(path, out):\n"
        "    with open(out, \"w\", encoding=\"utf-8\") as dest:\n"
        "        for row in csv_reader(path):\n"
        "            transformed = transform(row)\n"
        "            dest.write(\",\".join(transformed) + \"\\n\")\n"
        "\n"
        "# Bad: data = open(path).read().split()  → MemoryError on huge files"
        "</div>"
    ),
    18: (
        "<b>Cross-cutting concerns:</b> Decorators wrap once — retry, auth, timing."
        '<div class="step-pre">'
        "import time\n"
        "from functools import wraps\n"
        "\n"
        "def timer(fn):\n"
        "    @wraps(fn)\n"
        "    def wrapper(*args, **kwargs):\n"
        "        start = time.time()\n"
        "        result = fn(*args, **kwargs)\n"
        "        print(f\"{fn.__name__} took {time.time() - start:.2f}s\")\n"
        "        return result\n"
        "    return wrapper\n"
        "\n"
        "@timer\n"
        "def run_query():\n"
        "    time.sleep(0.1)\n"
        "    return \"ok\""
        "</div>"
    ),
    19: (
        "<b>File upload API:</b> Specific excepts + finally for cleanup."
        '<div class="step-pre">'
        "def upload(file, temp):\n"
        "    try:\n"
        "        save(file)\n"
        "        return {\"status\": 200}\n"
        "    except PermissionError:\n"
        "        return {\"status\": 403}\n"
        "    except OSError:\n"
        "        return {\"status\": 500}\n"
        "    finally:\n"
        "        temp.cleanup()   # always runs"
        "</div>"
    ),
    20: (
        "<b>Image resize service:</b> Threads for download (I/O); processes for CPU work."
        '<div class="step-pre">'
        "from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor\n"
        "\n"
        "def download(url):\n"
        "    return fetch_bytes(url)      # I/O-bound — GIL OK\n"
        "\n"
        "def heavy_resize(image_bytes):\n"
        "    return resize_pixels(image_bytes)  # CPU-bound\n"
        "\n"
        "with ThreadPoolExecutor() as pool:\n"
        "    images = list(pool.map(download, urls))\n"
        "\n"
        "with ProcessPoolExecutor() as pool:\n"
        "    out = list(pool.map(heavy_resize, images))"
        "</div>"
    ),
    21: (
        "<b>Notification fan-out:</b> Three network calls concurrently with gather."
        '<div class="step-pre">'
        "import asyncio\n"
        "\n"
        "async def send_email():\n"
        "    await asyncio.sleep(0.2)\n"
        '    return "email ok"\n'
        "\n"
        "async def send_sms():\n"
        "    await asyncio.sleep(0.2)\n"
        '    return "sms ok"\n'
        "\n"
        "async def push():\n"
        "    await asyncio.sleep(0.2)\n"
        '    return "push ok"\n'
        "\n"
        "async def notify():\n"
        "    results = await asyncio.gather(\n"
        "        send_email(),\n"
        "        send_sms(),\n"
        "        push(),\n"
        "    )\n"
        "    return results"
        "</div>"
    ),
    22: (
        "<b>Production order service:</b> Structured logs + exception traceback + rotation."
        '<div class="step-pre">'
        "import logging\n"
        "from logging.handlers import RotatingFileHandler\n"
        "\n"
        "logger = logging.getLogger(__name__)\n"
        "handler = RotatingFileHandler(\n"
        '    "app.log", maxBytes=1_000_000, backupCount=7\n'
        ")\n"
        "logger.addHandler(handler)\n"
        "logger.setLevel(logging.INFO)\n"
        "\n"
        "def pay(order_id):\n"
        "    try:\n"
        '        logger.info("order %s paid", order_id)\n'
        "    except Exception:\n"
        '        logger.exception("payment failed")'
        "</div>"
    ),
    23: (
        "<b>Discount engine CI:</b> Named test + mock so PRs never hit real payment APIs."
        '<div class="step-pre">'
        "from unittest.mock import patch\n"
        "\n"
        "def senior_discount(age, amount):\n"
        "    if age &gt;= 60:\n"
        "        return amount * 0.90\n"
        "    return amount\n"
        "\n"
        "def test_senior_citizen_gets_10_percent():\n"
        "    assert senior_discount(65, 1000) == 900\n"
        "\n"
        "@patch(\"payments.charge\")\n"
        "def test_checkout_mocks_gateway(mock_charge):\n"
        "    mock_charge.return_value = \"ok\"\n"
        "    assert checkout(100) == \"ok\""
        "</div>"
    ),
    24: (
        "<b>Log cleanup:</b> Find SSN-like patterns and redact before shipping to SIEM."
        '<div class="step-pre">'
        "import re\n"
        "\n"
        "pattern = r\"\\d{3}-\\d{2}-\\d{4}\"\n"
        "\n"
        "def redact(text):\n"
        "    matches = re.findall(pattern, text)\n"
        "    clean = text\n"
        "    for m in matches:\n"
        '        clean = clean.replace(m, "***-**-****")\n'
        "    return clean\n"
        "\n"
        'log = "user 123-45-6789 logged in"\n'
        "print(redact(log))"
        "</div>"
    ),
    25: (
        "<b>Daily sales export:</b> Read CSV, write JSON, make archive folder — auto-close."
        '<div class="step-pre">'
        "import csv\n"
        "import json\n"
        "from pathlib import Path\n"
        "\n"
        "def export_sales():\n"
        '    with open("sales.csv", encoding="utf-8") as f:\n'
        "        rows = list(csv.DictReader(f))\n"
        "\n"
        "    summary = {\"count\": len(rows)}\n"
        '    with open("summary.json", "w", encoding="utf-8") as out:\n'
        "        json.dump(summary, out, indent=2)\n"
        "\n"
        '    Path("archive").mkdir(exist_ok=True)'
        "</div>"
    ),
    26: (
        "<b>DB transaction helper:</b> Commit on success, rollback on error — like C# using."
        '<div class="step-pre">'
        "from contextlib import contextmanager\n"
        "\n"
        "@contextmanager\n"
        "def session_scope():\n"
        "    session = Session()\n"
        "    try:\n"
        "        yield session\n"
        "        session.commit()\n"
        "    except Exception:\n"
        "        session.rollback()\n"
        "        raise\n"
        "    finally:\n"
        "        session.close()\n"
        "\n"
        "with session_scope() as db:\n"
        "    db.add(order)"
        "</div>"
    ),
    27: (
        "<b>Two client projects:</b> Separate venvs so Django versions never clash."
        '<div class="step-pre">'
        "# Client A\n"
        "cd client_a\n"
        "python -m venv .venv\n"
        ".venv\\Scripts\\activate\n"
        "pip install -r requirements.txt   # Django 4.2\n"
        "\n"
        "# Client B\n"
        "cd client_b\n"
        "python -m venv .venv\n"
        ".venv\\Scripts\\activate\n"
        "pip install -r requirements.txt   # Django 5"
        "</div>"
    ),
    28: (
        "<b>Internal HR API:</b> Route → Pydantic → service → SQLAlchemy → response schema."
        '<div class="step-pre">'
        "@app.post(\"/employees\", response_model=EmployeeRead)\n"
        "def create_employee(\n"
        "    body: EmployeeCreate,\n"
        "    db: Session = Depends(get_db),\n"
        "):\n"
        "    emp = Employee(**body.model_dump())\n"
        "    db.add(emp)\n"
        "    db.commit()\n"
        "    db.refresh(emp)\n"
        "    return emp   # serialized via EmployeeRead, not raw ORM"
        "</div>"
    ),
    29: (
        "<b>Interview demo path:</b> One story from basics → regex → web API → voice AI."
        '<div class="step-pre">'
        "# Demo order in Python-Set2\n"
        "python pythonBasics/MyClass/car.py\n"
        "python google-python-exercises/babynames/babynames.py\n"
        "# then show Django / DRF API\n"
        "# then show Pipecat voice POC"
        "</div>"
    ),
    30: (
        "<b>Team onboarding:</b> New joiners open topic folders that map to slides."
        '<div class="step-pre">'
        "# Clone → open modules\n"
        "cd Python-Set2/pythonBasics\n"
        "python MyClass/oops_inheritance_BankAccount.py   # ↔ slide 15 OOP\n"
        "python MyUnitTesting/calculator_unittest.py      # ↔ slide 23 tests"
        "</div>"
    ),
    31: (
        "<b>Data analyst task:</b> Clean Titanic CSV, group, present to stakeholders."
        '<div class="step-pre">'
        "import pandas as pd\n"
        "\n"
        "df = pd.read_csv(\"titanic.csv\")\n"
        "df = df.dropna(subset=[\"Age\"])\n"
        "\n"
        "summary = (\n"
        "    df.groupby(\"Survived\")[\"Age\"]\n"
        "      .mean()\n"
        ")\n"
        "print(summary)\n"
        "# present chart in Jupyter to stakeholders"
        "</div>"
    ),
    32: (
        "<b>Meeting planner product:</b> Django site + DRF JSON + later async microservice."
        '<div class="step-pre">'
        "# Django view (MVT)\n"
        "def room_list(request):\n"
        "    rooms = Room.objects.filter(available=True)\n"
        '    return render(request, "rooms.html", {"rooms": rooms})\n'
        "\n"
        "# DRF API for mobile\n"
        "class RoomViewSet(viewsets.ModelViewSet):\n"
        "    queryset = Room.objects.all()\n"
        "    serializer_class = RoomSerializer"
        "</div>"
    ),
    33: (
        "<b>Clinic phone bot:</b> STT → LLM → TTS chain (Pipecat-style processors)."
        '<div class="step-pre">'
        "async def handle_turn(audio_chunk):\n"
        "    text = await stt.transcribe(audio_chunk)\n"
        "    if \"member\" in text.lower():\n"
        "        reply = await llm.ask(\"Validate member ID\")\n"
        "    else:\n"
        '        reply = "Please say your member ID"\n'
        "    speech = await tts.speak(reply)\n"
        "    return speech"
        "</div>"
    ),
    34: (
        "<b>Greenfield microservice:</b> Controllers / Services / DTOs style layout."
        '<div class="step-pre">'
        "# project layout\n"
        "app/\n"
        "  routes/          # thin HTTP handlers\n"
        "  services/        # business rules\n"
        "  schemas/         # Pydantic DTOs\n"
        "  models/          # DB / ORM\n"
        "tests/              # at repo root\n"
        "\n"
        "# routes call services — not raw SQL"
        "</div>"
    ),
    35: (
        "<b>C# shop adopting Python:</b> Map familiar ideas so .NET devs ramp fast."
        '<div class="step-pre">'
        "# C# null          →  None\n"
        "# C# using (...)   →  with open(...) as f:\n"
        "# C# async Task    →  async def fn():\n"
        "# C# NuGet         →  pip + venv\n"
        "# C# empty { }     →  pass\n"
        "\n"
        "def save_report():\n"
        "    pass   # stub — like empty method body\n"
        "\n"
        "value = None\n"
        "if value is None:\n"
        '    print("no data")'
        "</div>"
    ),
}


def real_life_for(n: int) -> str:
    text = REAL_LIFE.get(n)
    if not text:
        return ""
    return f'<div class="real-life"><b>Real-life example:</b> {text}</div>'
