# 01 Lists/Tuples/Sets — mutation, slicing, unpacking, namedtuple, set operations
# 02 Dictionaries — get, update, pop, iterating keys/values/items
# 03 Comprehensions — list/dict/set comprehensions, generator expressions, nested
# 04 Functions — defaults, *args/**kwargs, keyword-only args, nonlocal scope
# 05 Lambda & Recursion — lambda with sorted/filter/map, recursive factorial, memoized Fibonacci
# 06 Modules & Packages — stdlib imports, package layout explained, plus a live demo building and importing a module on the fly (no stray files left behind)
# 07 File Handling — write/append/read modes, line iteration, all via a temp dir that cleans itself up
# 08 Exception Handling — multiple except, else/finally, a custom InsufficientFundsError
# 09 OOP — inheritance, super(), encapsulation convention, dunder __str__, polymorphism
# 10 Iterators & Generators — a hand-written iterator class vs. an equivalent yield-based generator
# 11 CSV & JSON — csv.DictWriter/DictReader, json.dump/load/dumps/loads
# 12 Debugging & Testing — assert, logging, a minimal hand-rolled test runner, a note on breakpoint()
# 13 Mini-Projects — a JSON-persisted To-Do list (OOP + file + JSON) and a word-frequency counter (Counter + comprehensions)


"""
Python Basic II - Data Structures, Functions & Beyond
=============================================================
Run this file directly to see every section's output:
    python Python-Basics-2.py
"""

import csv
import importlib.util
import json
import logging
import os
import tempfile
from collections import Counter, namedtuple


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# =====================================================================
# 01. Lists, Tuples, Sets
# =====================================================================

def topic_01_lists_tuples_sets():
    section("01. Lists, Tuples, Sets")

    # --- Lists: ordered, mutable, allow duplicates ---
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    fruits.insert(1, "avocado")
    fruits.remove("banana")
    fruits.sort()
    print("list:", fruits)
    print("sliced [1:3]:", fruits[1:3])

    # --- Tuples: ordered, immutable, allow duplicates ---
    point = (3, 4)
    x, y = point  # unpacking
    print(f"tuple: {point} -> x={x}, y={y}")

    Point = namedtuple("Point", ["x", "y"])
    p2 = Point(5, 6)
    print("namedtuple:", p2, "p2.x =", p2.x)

    # --- Sets: unordered, mutable, no duplicates ---
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("set a:", a, "| set b:", b)
    print("union:", a | b)
    print("intersection:", a & b)
    print("difference (a-b):", a - b)
    a.add(10)
    a.discard(1)
    print("after add/discard:", a)


# =====================================================================
# 02. Dictionaries
# =====================================================================

def topic_02_dictionaries():
    section("02. Dictionaries")

    student = {"name": "Shumyla", "age": 30, "course": "Python"}
    print("dict:", student)

    print("get('age'):", student.get("age"))
    print("get('grade', 'N/A'):", student.get("grade", "N/A"))

    student.update({"age": 31, "grade": "A"})
    print("after update:", student)

    removed = student.pop("grade")
    print(f"popped {removed!r}, remaining:", student)

    print("keys:", list(student.keys()))
    print("values:", list(student.values()))
    print("items:")
    for key, value in student.items():
        print(f"  {key} -> {value}")

    print("'name' in student?", "name" in student)


# =====================================================================
# 03. Comprehensions
# =====================================================================

def topic_03_comprehensions():
    section("03. Comprehensions")

    # List comprehension
    squares = [n * n for n in range(1, 11)]
    print("squares:", squares)

    # List comprehension with a condition
    even_squares = [n * n for n in range(1, 11) if n % 2 == 0]
    print("even squares:", even_squares)

    # Dict comprehension
    square_map = {n: n * n for n in range(1, 6)}
    print("square_map:", square_map)

    # Set comprehension
    unique_lengths = {len(word) for word in ["cat", "dog", "mouse", "ox"]}
    print("unique word lengths:", unique_lengths)

    # Generator expression (lazy - computed on demand, not stored in memory)
    gen = (n * n for n in range(1, 6))
    print("generator expression consumed:", list(gen))

    # Nested comprehension (flatten a 2D grid)
    grid = [[1, 2, 3], [4, 5, 6]]
    flattened = [value for row in grid for value in row]
    print("flattened grid:", flattened)


# =====================================================================
# 04. Functions
# =====================================================================

def describe_person(name, age=18, *hobbies, country="unknown", **extra):
    """Demonstrates positional, default, *args, keyword-only, **kwargs."""
    print(f"{name} ({age}) from {country}")
    if hobbies:
        print("  hobbies:", ", ".join(hobbies))
    if extra:
        print("  extra info:", extra)


def min_max(numbers):
    """Returns multiple values as a tuple."""
    return min(numbers), max(numbers)


def topic_04_functions():
    section("04. Functions")

    describe_person("Shumyla")
    describe_person("Ali", 25, "chess", "reading", country="Pakistan", city="Lahore")

    low, high = min_max([4, 1, 9, 2, 7])
    print(f"min={low}, max={high}")

    # Scope: local vs global
    counter = 0

    def increment():
        nonlocal counter
        counter += 1

    increment()
    increment()
    print("counter after two increments:", counter)


# =====================================================================
# 05. Lambda and Recursion
# =====================================================================

def topic_05_lambda_and_recursion():
    section("05. Lambda and Recursion")

    # Lambda: a small anonymous function
    square = lambda n: n * n
    print("square(7) =", square(7))

    words = ["banana", "fig", "apple", "kiwi"]
    print("sorted by length:", sorted(words, key=lambda w: len(w)))
    print("filter len>4:", list(filter(lambda w: len(w) > 4, words)))
    print("map upper:", list(map(lambda w: w.upper(), words)))

    # Plain recursion: factorial
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print("factorial(6) =", factorial(6))

    # Recursion with memoization (avoids recomputing the same calls)
    memo = {}

    def fib(n):
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

    print("fibonacci(20) =", fib(20))


# =====================================================================
# 06. Modules and Packages
# =====================================================================

def topic_06_modules_and_packages():
    section("06. Modules and Packages")

    # Standard library modules - several import styles
    import math
    import random
    from datetime import date

    print("math.sqrt(49) =", math.sqrt(49))
    random.seed(42)
    print("random.randint(1, 100) =", random.randint(1, 100))
    print("today =", date.today())

    # A "package" is just a folder with an __init__.py containing
    # modules, e.g.:
    #   mypackage/
    #       __init__.py
    #       utils.py        -> import mypackage.utils
    #       sub/
    #           __init__.py
    #           tools.py     -> import mypackage.sub.tools

    # Demonstrating "your own module" without leaving a stray file in
    # the project: write a tiny module to a temp folder and import it.
    with tempfile.TemporaryDirectory() as tmp_dir:
        module_path = os.path.join(tmp_dir, "greeting_module.py")
        with open(module_path, "w", encoding="utf-8") as f:
            f.write("def say_hello(name):\n    return f'Hello, {name}, from a custom module!'\n")

        spec = importlib.util.spec_from_file_location("greeting_module", module_path)
        greeting_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(greeting_module)

        print(greeting_module.say_hello("Shumyla"))


# =====================================================================
# 07. File Handling
# =====================================================================

def topic_07_file_handling():
    section("07. File Handling")

    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, "notes.txt")

        # Write mode ('w') overwrites the file if it already exists
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Line 1: Python file handling\n")
            f.write("Line 2: using the 'with' statement\n")

        # Append mode ('a') adds to the end without erasing existing content
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("Line 3: appended afterwards\n")

        # Read mode ('r') - whole file, then line by line
        with open(file_path, "r", encoding="utf-8") as f:
            print("Full contents:\n" + f.read())

        with open(file_path, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                print(f"  line {line_number}: {line.rstrip()}")

        print("File exists?", os.path.exists(file_path))
    # tmp_dir and its contents are automatically removed here


# =====================================================================
# 08. Exception Handling
# =====================================================================

class InsufficientFundsError(Exception):
    """Custom exception for a simple bank-account example."""
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw {amount}, balance is only {balance}"
        )
    return balance - amount


def topic_08_exception_handling():
    section("08. Exception Handling")

    # Multiple except clauses for different error types
    for value in ["10", "abc", "0"]:
        try:
            result = 100 / int(value)
        except ValueError:
            print(f"'{value}' is not a valid number")
        except ZeroDivisionError:
            print(f"'{value}' caused a division by zero")
        else:
            # 'else' runs only if no exception was raised
            print(f"100 / {value} = {result}")
        finally:
            print(f"  (done checking '{value}')")

    # Custom exception in action
    try:
        withdraw(100, 150)
    except InsufficientFundsError as e:
        print("Custom exception caught:", e)


# =====================================================================
# 09. Object-Oriented Programming
# =====================================================================

class Animal:
    """Base class demonstrating encapsulation and dunder methods."""

    def __init__(self, name, sound):
        self.name = name
        self._sound = sound  # "protected" by convention (single underscore)

    def speak(self):
        return f"{self.name} says {self._sound}"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    """Subclass demonstrating inheritance, super(), and overriding."""

    def __init__(self, name):
        super().__init__(name, "Woof")

    def speak(self):
        base_sound = super().speak()
        return f"{base_sound} (wags tail)"


def topic_09_oop():
    section("09. Object-Oriented Programming")

    generic = Animal("Generic Animal", "...")
    dog = Dog("Rex")

    print(generic.speak())
    print(dog.speak())
    print("str(dog):", str(dog))  # falls back to Animal.__str__

    # Polymorphism: same method name, different behavior per subclass
    for animal in [generic, dog]:
        print(" polymorphic call ->", animal.speak())


# =====================================================================
# 10. Iterators and Generators
# =====================================================================

class CountDown:
    """A custom iterator counting down to zero."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def countdown_generator(start):
    """The same idea, written as a generator function with 'yield'."""
    while start >= 0:
        yield start
        start -= 1


def topic_10_iterators_and_generators():
    section("10. Iterators and Generators")

    print("custom iterator:", list(CountDown(3)))
    print("generator function:", list(countdown_generator(3)))

    # Generators compute values lazily, one at a time, via next()
    gen = countdown_generator(2)
    print("next(gen) ->", next(gen))
    print("next(gen) ->", next(gen))
    print("next(gen) ->", next(gen))


# =====================================================================
# 11. CSV and JSON
# =====================================================================

def topic_11_csv_and_json():
    section("11. CSV and JSON")

    rows = [
        {"name": "Shumyla", "role": "Developer"},
        {"name": "Ali", "role": "Analyst"},
    ]

    with tempfile.TemporaryDirectory() as tmp_dir:
        # --- CSV ---
        csv_path = os.path.join(tmp_dir, "people.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "role"])
            writer.writeheader()
            writer.writerows(rows)

        print("CSV file written, reading it back:")
        with open(csv_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                print(" ", dict(row))

        # --- JSON ---
        json_path = os.path.join(tmp_dir, "people.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2)

        with open(json_path, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        print("JSON round-trip loaded:", loaded)

        # json.dumps()/loads() work directly on strings too (no file needed)
        as_text = json.dumps({"ok": True, "count": 2})
        print("json.dumps:", as_text)
        print("json.loads:", json.loads(as_text))


# =====================================================================
# 12. Debugging and Testing
# =====================================================================

def add(a, b):
    return a + b


def run_tiny_test_suite():
    """A minimal hand-rolled test runner (see also: the 'unittest' and
    'pytest' libraries for real projects)."""
    checks = [
        ("add(2, 3) == 5", add(2, 3) == 5),
        ("add(-1, 1) == 0", add(-1, 1) == 0),
        ("is_prime-like check", 7 % 2 == 1),
    ]
    passed = 0
    for description, outcome in checks:
        status = "PASS" if outcome else "FAIL"
        if outcome:
            passed += 1
        print(f"  [{status}] {description}")
    print(f"{passed}/{len(checks)} checks passed")


def topic_12_debugging_and_testing():
    section("12. Debugging and Testing")

    # assert: cheap sanity checks (disabled if Python runs with -O)
    assert add(2, 2) == 4, "add() is broken!"
    print("assert add(2, 2) == 4 passed silently")

    # logging: better than scattering print() through real projects
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger("python_basics_2")
    logger.info("This is an info-level log message")
    logger.warning("This is a warning-level log message")

    # A minimal test suite
    run_tiny_test_suite()

    # Debugging note: in real debugging sessions you'd drop a
    # breakpoint() (or `import pdb; pdb.set_trace()`) at the line you
    # want to pause on, then step through with an interactive debugger.
    # Not invoked here since it would halt this script.


# =====================================================================
# 13. Mini-Projects
# =====================================================================

class ToDoList:
    """Mini-project 1: a to-do list with JSON persistence (ties
    together OOP + file handling + JSON)."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.items = []
        self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.items = json.load(f)

    def _save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.items, f, indent=2)

    def add(self, task):
        self.items.append({"task": task, "done": False})
        self._save()

    def complete(self, index):
        self.items[index]["done"] = True
        self._save()

    def pending(self):
        return [item["task"] for item in self.items if not item["done"]]

    def __str__(self):
        lines = []
        for i, item in enumerate(self.items):
            mark = "x" if item["done"] else " "
            lines.append(f"  [{mark}] {i}: {item['task']}")
        return "\n".join(lines) if lines else "  (empty)"


def word_frequency(text, top_n=3):
    """Mini-project 2: word-frequency counter (ties together strings +
    comprehensions + collections.Counter)."""
    words = [w.strip(".,!?").lower() for w in text.split()]
    counts = Counter(words)
    return counts.most_common(top_n)


def topic_13_mini_projects():
    section("13. Mini-Projects")

    print("--- Mini-Project 1: To-Do List (JSON-backed) ---")
    with tempfile.TemporaryDirectory() as tmp_dir:
        todo_path = os.path.join(tmp_dir, "todo.json")
        todo = ToDoList(todo_path)
        todo.add("Learn Python basics")
        todo.add("Practice comprehensions")
        todo.add("Build a mini project")
        todo.complete(1)
        print(todo)
        print("pending:", todo.pending())

        # Reload from disk to prove persistence worked
        reloaded = ToDoList(todo_path)
        print("reloaded from disk:")
        print(reloaded)

    print("\n--- Mini-Project 2: Word Frequency Counter ---")
    sample_text = (
        "Python is great. Python is readable. "
        "Learning Python is fun, and Python is powerful!"
    )
    print("text:", sample_text)
    print("top 3 words:", word_frequency(sample_text, top_n=3))


if __name__ == "__main__":
    topic_01_lists_tuples_sets()
    topic_02_dictionaries()
    topic_03_comprehensions()
    topic_04_functions()
    topic_05_lambda_and_recursion()
    topic_06_modules_and_packages()
    topic_07_file_handling()
    topic_08_exception_handling()
    topic_09_oop()
    topic_10_iterators_and_generators()
    topic_11_csv_and_json()
    topic_12_debugging_and_testing()
    topic_13_mini_projects()

    print("\nPython Basics 2 - script ran successfully.")
