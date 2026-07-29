# Day 10 – Dictionaries & JSON (LEARNINGS.md)

**Date:** July 21, 2026

---

# Overview

Today I learned about **Dictionaries** and **JSON** in Python. Dictionaries store data as key-value pairs and are ideal for structured information like student records, product inventories, and application settings. JSON (JavaScript Object Notation) is the standard format for saving data to files and communicating with APIs — critical for AI engineering.

I completed three practical tasks:
1. Student Information System
2. Product Inventory Manager
3. Configuration Manager

---

# Concepts Learned

## 1. Dictionaries

### What I Learned
- Dictionaries store data as `{key: value}` pairs
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any data type — strings, numbers, lists, even other dictionaries
- Lookup by key is O(1) — very fast compared to searching lists
- Dictionaries are mutable — you can add, update, and remove entries

### Example

```python
student = {"name": "Awais", "age": 19, "course": "AI Engineering"}
print(student["name"])  # Awais
```

---

## 2. Dictionary Methods

### What I Learned

| Method | Purpose |
|--------|---------|
| `get(key, default)` | Safe access — returns default if key missing |
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `update(other)` | Merge another dictionary |
| `pop(key)` | Remove key and return its value |

### Why `.get()` Matters

```python
# This raises KeyError if "email" doesn't exist:
# email = student["email"]

# This returns a default safely:
email = student.get("email", "Not provided")
```

---

## 3. Nested Dictionaries

### What I Learned
- Dictionaries can contain other dictionaries for complex data
- Common pattern: `{id: {field1, field2, nested_dict}}`
- Access nested values with chained brackets: `data["S001"]["grades"]["Python"]`

---

## 4. Dictionary Comprehension

### What I Learned
- Create dictionaries in one line: `{key: value for item in iterable}`
- Can include conditions: `{k: v for k, v in items if condition}`

---

## 5. JSON (JavaScript Object Notation)

### What I Learned
- JSON is a text format for storing and exchanging data
- Used everywhere in AI: API responses, config files, LangChain documents
- `json.dump()` / `json.load()` for files; `json.dumps()` / `json.loads()` for strings

---

# Practical Tasks

## Task 1: Student Information System
- Nested dictionary with grades, GPA calculation, JSON save/load, performance report

## Task 2: Product Inventory Manager
- Product tracking, category search, low stock alerts, JSON export

## Task 3: Configuration Manager
- Load/validate config.json, defaults for missing keys, programmatic updates

---

# Research Comparison

| Source | Key Points | Clarity (1-5) |
|--------|-----------|---------------|
| ChatGPT | Dicts as hash maps, O(1) lookup | 4 |
| Gemini | Nested dicts, JSON in REST APIs | 4 |
| Claude | `.get()` patterns, config files | 5 |
| Python Docs | Official syntax, json module | 5 |

**Clearest Explanation:** Claude — practical config and safe access patterns.

---

# Key Takeaways

1. Dictionaries are the main way to store structured data in Python.
2. Use `.get(key, default)` to avoid KeyError on missing keys.
3. JSON lets you persist data and exchange it with APIs.
4. These skills prepare directly for LangChain metadata and API configs (Week 3).

---

# References

- ChatGPT (Consulted: July 21, 2026)
- Google Gemini (Consulted: July 21, 2026)
- Claude AI (Consulted: July 21, 2026)
- Python Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

---

**Prepared by:** Muhammad Awais Ramzan — AI Engineering Intern, Day 10
