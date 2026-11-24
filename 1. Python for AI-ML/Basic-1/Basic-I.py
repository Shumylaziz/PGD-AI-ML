 variables/types, strings, lists, dicts, conditionals, loops, functions, and a simple class."""
Python Basic I - Programming Fundamentals (Beginner level)
=============================================================
Covers topics 01-15 of the "01-Python/Basic-I" curriculum, each with
runnable examples, followed by the 10 recommended practice exercises.

Run this file directly to see every section's output:
    python Python-Basics-1.py
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# =====================================================================
# 01. Introduction to Python
# =====================================================================
# - History: created by Guido van Rossum, first released in 1991.
# - Features: easy to read, interpreted, dynamically typed, huge
#   standard library, large ecosystem (pip packages).
# - Installation: download from python.org, or use a distribution
#   like Anaconda. Check your version from a terminal with:
#       python --version
# - IDEs/editors commonly used: VS Code, PyCharm, Jupyter Notebook,
#   Google Colab, IDLE (ships with Python).


# =====================================================================
# 02. Python Environment
# =====================================================================
# - Jupyter Notebook: runs in the browser, mixes code + text + output
#   in "cells" - great for data analysis and learning.
# - Google Colab: a free, cloud-hosted Jupyter Notebook (no install).
# - VS Code: a lightweight code editor with a Python extension that
#   adds debugging, linting, and an integrated terminal.
# This file is a plain ".py" script, meant to be run from a terminal
# or an editor's "Run" button rather than cell-by-cell.


def topic_03_syntax():
    section("03. Python Syntax")
    # Indentation defines code blocks (no curly braces like PL/SQL
    # BEGIN/END or C-style {}). Standard indent is 4 spaces.
    if True:
        print("This line is indented 4 spaces - it belongs to the if block.")

    # Comments start with '#' and run to the end of the line.
    # A string on its own, especially a triple-quoted one, is often
    # used as a "docstring" to document a module/function/class.

    # A statement is one instruction; multiple statements can share a
    # line separated by ';' (rarely used, one-per-line is preferred).
    x = 1; y = 2
    print("x + y =", x + y)


def topic_04_variables():
    section("04. Variables")
    # Naming conventions: snake_case for variables/functions,
    # must start with a letter or underscore, no spaces, case-sensitive,
    # cannot be a reserved word (if, for, class, ...).
    name = "Shumyla"
    age = 30
    height = 5.6
    is_student = False

    print(name, age, height, is_student)

    # Multiple assignment and reassignment
    a, b, c = 1, 2, 3
    print("a, b, c =", a, b, c)
    a = "now a string"
    print("a reassigned to:", a)


def topic_05_data_types():
    section("05. Data Types")
    an_int = 42
    a_float = 3.14
    a_str = "hello"
    a_bool = True

    print(an_int, type(an_int))
    print(a_float, type(a_float))
    print(a_str, type(a_str))
    print(a_bool, type(a_bool))


def topic_06_type_conversion():
    section("06. Type Conversion")
    # Implicit conversion: Python promotes int -> float automatically
    result = 5 + 2.0
    print("5 + 2.0 =", result, type(result))

    # Explicit conversion: you call int(), float(), str(), bool()
    text_number = "123"
    as_int = int(text_number)
    print("int('123') =", as_int, type(as_int))

    as_str = str(99)
    print("str(99) =", as_str, type(as_str))

    print("float('3.5') =", float("3.5"))
    print("bool(0), bool(1), bool(''), bool('x') =",
          bool(0), bool(1), bool(""), bool("x"))


def topic_07_operators():
    section("07. Operators")
    a, b = 10, 3

    # Arithmetic
    print("Arithmetic:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

    # Comparison
    print("Comparison:", a == b, a != b, a > b, a < b, a >= b, a <= b)

    # Logical
    print("Logical:", (a > 5) and (b < 5), (a > 5) or (b > 5), not (a > 5))


def topic_08_input_output():
    section("08. Input and Output")
    # print() with formatting
    name = "Shumyla"
    score = 95.5
    print(f"{name} scored {score:.1f} points")        # f-string
    print("{} scored {:.1f} points".format(name, score))  # .format()
    print("%s scored %.1f points" % (name, score))     # % formatting

    # input() reads a line of text from the user as a string.
    # Guarded here so the script still runs fine with no console input
    # attached (e.g. when run non-interactively).
    try:
        user_name = input("Enter your name (press Enter to skip): ")
        if user_name:
            print(f"Hello, {user_name}!")
        else:
            print("No name entered - skipping.")
    except EOFError:
        print("No input stream available - skipping input() demo.")


def topic_09_strings():
    section("09. String Fundamentals")
    s = "Python Basics"

    # Indexing (0-based) and negative indexing
    print("s[0] =", s[0], " s[-1] =", s[-1])

    # Slicing: s[start:stop:step]
    print("s[0:6] =", s[0:6])
    print("s[7:] =", s[7:])
    print("s[::-1] =", s[::-1])  # reversed

    # Common string methods
    print("upper():", s.upper())
    print("lower():", s.lower())
    print("replace():", s.replace("Basics", "Rocks"))
    print("split():", s.split(" "))
    print("strip():", "  padded  ".strip())
    print("find('Basics'):", s.find("Basics"))
    print("len(s):", len(s))


def topic_10_conditionals():
    section("10. Conditional Statements")
    age = 20

    if age < 13:
        category = "child"
    elif age < 20:
        category = "teenager"
    else:
        category = "adult"
    print(f"Age {age} -> {category}")

    # Nested if
    num = 15
    if num > 0:
        if num % 2 == 0:
            print(f"{num} is positive and even")
        else:
            print(f"{num} is positive and odd")
    else:
        print(f"{num} is not positive")


def topic_11_loops():
    section("11. Loops")
    # for loop over a range
    for i in range(5):
        print("for i in range(5):", i)

    # for loop over a collection
    for fruit in ["apple", "banana", "cherry"]:
        print("fruit:", fruit)

    # while loop
    count = 0
    while count < 3:
        print("while count =", count)
        count += 1

    # nested loops (simple multiplication grid)
    for row in range(1, 4):
        line = ""
        for col in range(1, 4):
            line += f"{row * col:4}"
        print(line)


def topic_12_loop_control():
    section("12. Loop Control")
    # break - exit the loop early
    for i in range(10):
        if i == 4:
            break
        print("break demo, i =", i)

    # continue - skip to the next iteration
    for i in range(6):
        if i % 2 == 0:
            continue
        print("continue demo, odd i =", i)

    # pass - a no-op placeholder (useful while sketching code)
    for i in range(3):
        if i == 1:
            pass  # TODO: handle this case later
        print("pass demo, i =", i)


def topic_13_basic_collections():
    section("13. Basic Collections")
    # Lists: ordered, mutable
    numbers = [1, 2, 3]
    numbers.append(4)
    numbers[0] = 100
    print("list:", numbers)

    # Tuples: ordered, immutable
    point = (3, 4)
    print("tuple:", point, "x =", point[0], "y =", point[1])
    try:
        point[0] = 99  # raises TypeError - tuples can't be modified
    except TypeError as e:
        print("Can't modify a tuple:", e)


def topic_14_error_handling():
    section("14. Basic Error Handling")
    # Syntax errors happen before the code even runs (e.g. a missing
    # colon) - Python won't let you execute code with one.

    # Runtime errors happen while the code is running and can be
    # caught with try/except so the program doesn't crash.
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught a runtime error:", e)

    try:
        value = int("not a number")
    except ValueError as e:
        print("Caught another runtime error:", e)
    finally:
        print("finally block always runs, for cleanup code")


# =====================================================================
# 15. Practice Exercises
# =====================================================================

def simple_calculator(a, b, operator):
    """Basic calculator: operator is one of + - * /"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    return "Error: unknown operator"


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def grade_calculator(marks):
    """marks: 0-100 -> letter grade"""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def is_even(number):
    return number % 2 == 0


def multiplication_table(number, up_to=10):
    return [f"{number} x {i} = {number * i}" for i in range(1, up_to + 1)]


def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def fibonacci_sequence(count):
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def number_guessing_game(secret_number, guesses):
    """Non-interactive version: takes a list of guesses and reports
    the result of each one, so it can run without blocking on input()."""
    results = []
    for guess in guesses:
        if guess < secret_number:
            results.append(f"{guess}: too low")
        elif guess > secret_number:
            results.append(f"{guess}: too high")
        else:
            results.append(f"{guess}: correct!")
            break
    return results


def run_practice_exercises():
    section("15. Practice Exercises")

    print("Simple calculator: 7 + 5 =", simple_calculator(7, 5, "+"))
    print("Simple calculator: 7 / 0 =", simple_calculator(7, 0, "/"))

    print("Temperature: 100C in F =", celsius_to_fahrenheit(100))
    print("Temperature: 32F in C =", fahrenheit_to_celsius(32))

    print("Grade for 85 marks:", grade_calculator(85))

    print("Is 7 even?", is_even(7), "| Is 8 even?", is_even(8))

    print("Multiplication table for 5:")
    for line in multiplication_table(5):
        print(" ", line)

    print("Factorial of 5:", factorial(5))

    print("Is 17 prime?", is_prime(17), "| Is 18 prime?", is_prime(18))

    print("First 10 Fibonacci numbers:", fibonacci_sequence(10))

    print("Is 'madam' a palindrome?", is_palindrome("madam"))
    print("Is 'hello' a palindrome?", is_palindrome("hello"))

    print("Number guessing game (secret=42):",
          number_guessing_game(42, [10, 50, 40, 42]))


if __name__ == "__main__":
    topic_03_syntax()
    topic_04_variables()
    topic_05_data_types()
    topic_06_type_conversion()
    topic_07_operators()
    topic_08_input_output()
    topic_09_strings()
    topic_10_conditionals()
    topic_11_loops()
    topic_12_loop_control()
    topic_13_basic_collections()
    topic_14_error_handling()
    run_practice_exercises()

    print("\nPython Basics 1 - script ran successfully.")
