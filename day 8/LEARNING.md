# Day 8 – Lists & List Operations

## Overview
Today I learned how Python lists work and how they can be used to store, manage, and manipulate collections of data efficiently. I practiced performing common operations on lists and built real-world projects using list methods, slicing, and list comprehensions.

---

# Concepts Learned

## 1. Lists in Python
- Lists are **ordered** collections that preserve the order of inserted elements.
- Lists are **mutable**, meaning their values can be changed after creation.
- A single list can store different data types such as integers, strings, floats, booleans, and even other lists.
- Lists are created using square brackets `[]`.

### Example

```python
numbers = [10, 20, 30]
names = ["Ali", "Awais", "Ahmed"]
mixed = [10, "Python", 3.14, True]
```

---

## 2. List Methods

### `append()`
Adds an item to the end of the list.

```python
students.append("Ali")
```

### `insert()`
Inserts an item at a specific index.

```python
students.insert(0, "Ahmed")
```

### `remove()`
Removes the first occurrence of a specified value.

```python
students.remove("Ali")
```

### `pop()`
Removes an item by index and returns it.

```python
students.pop(2)
```

### `sort()`
Sorts the list in ascending order.

```python
grades.sort()
```

### `reverse()`
Reverses the order of list elements.

```python
grades.reverse()
```

### `clear()`
Removes all elements from the list.

```python
students.clear()
```

---

## 3. List Slicing

List slicing allows access to specific portions of a list.

### Syntax

```python
list[start:end:step]
```

### Examples

```python
numbers[:5]
numbers[2:7]
numbers[-3:]
numbers[::-1]
```

### Learned
- Positive indexing
- Negative indexing
- Reversing a list
- Selecting every second element
- Extracting sublists

---

## 4. List Comprehensions

List comprehensions provide a concise way to create new lists.

### Syntax

```python
[new_value for item in iterable if condition]
```

### Examples

```python
squares = [x * x for x in range(10)]

even_numbers = [x for x in numbers if x % 2 == 0]

clean_names = [name.strip().lower() for name in names]
```

### Benefits
- Less code
- Better readability
- Faster than traditional loops for many simple tasks

---

## 5. When to Use Lists

Use lists when:
- Order of data matters.
- Elements need to be modified.
- Frequent indexing is required.
- Data needs to be added or removed dynamically.
- Managing collections like students, products, shopping carts, or records.

---

# Practical Tasks

## Task 1 – Student Grade Manager

### Features
- Store student names and grades
- Add new students
- Remove students
- Update grades
- Calculate average grade
- Find highest and lowest grades
- Sort students by grades (descending)
- Display top 3 performers
- Filter students above and below average using list comprehensions

### Skills Practiced
- Parallel lists
- Functions
- Loops
- `max()`
- `min()`
- `zip()`
- `sorted()`
- List comprehensions

---

## Task 2 – Shopping Cart System

### Features
- Add items
- Remove items
- Update quantities
- Calculate total bill
- Apply 10% discount when total exceeds $100
- Display an itemized receipt
- Show recently added items using list slicing

### Skills Practiced
- Parallel lists
- Arithmetic operations
- Conditional statements
- Formatted printing
- List slicing

---

## Task 3 – Data Cleaning Pipeline

### Cleaning Steps
- Remove `None` values
- Remove extra whitespace
- Convert text to lowercase
- Remove duplicate values
- Compare data quality before and after cleaning

### Skills Practiced
- List comprehensions
- String methods
- Data preprocessing
- Duplicate removal
- Data quality metrics

---

# Python Functions & Methods Used

- `append()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`
- `clear()`
- `len()`
- `sum()`
- `max()`
- `min()`
- `enumerate()`
- `zip()`
- `sorted()`

---

# Challenges Faced

- Keeping student names and grades synchronized in parallel lists.
- Sorting students while maintaining correct name-grade relationships.
- Understanding list slicing with different start, end, and step values.
- Removing duplicates while preserving the original order.
- Writing list comprehensions for data cleaning tasks.

---

# Key Takeaways

- Lists are one of the most commonly used data structures in Python.
- List methods make data manipulation simple and efficient.
- List slicing provides quick access to subsets of data.
- List comprehensions produce cleaner and more readable code.
- Lists are ideal for real-world applications such as student management systems, shopping carts, and data cleaning pipelines.

---

# References

- ChatGPT
- Google Gemini
- Claude AI
- Python Official Documentation: https://docs.python.org/3/tutorial/datastructures.html