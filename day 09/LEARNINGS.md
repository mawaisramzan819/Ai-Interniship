# Day 9 – Tuples & Sets (LEARNINGS.md)

**Date:** July 20, 2026

---

# Overview

Today I learned about **Tuples** and **Sets** in Python. I understood how tuples are used for storing fixed data that should not change, while sets are useful for storing unique values and performing mathematical set operations such as union, intersection, and difference.

I also completed three practical tasks:
1. Geographic Coordinates System
2. Unique Visitor Tracker
3. Email Validation System

---

# Concepts Learned

## 1. Tuples

### What I Learned
- Tuples are ordered collections.
- Tuples are immutable (cannot be changed after creation).
- They can store multiple data types.
- Tuples are faster than lists because they are immutable.
- They are commonly used for fixed information like coordinates, RGB colors, and database records.

### Example

```python
city = ("Lahore", 31.5204, 74.3587)
```

---

## 2. Tuple Packing and Unpacking

### What I Learned

Tuple Packing:
- Multiple values are packed into one tuple.

```python
person = ("Awais", 19, "Pakistan")
```

Tuple Unpacking:
- Values are extracted into separate variables.

```python
name, age, country = person
```

Functions can also return multiple values using tuples.

```python
def get_data():
    return "Awais", 19

name, age = get_data()
```

---

## 3. Sets

### What I Learned

- Sets store unique values only.
- Duplicate values are automatically removed.
- Sets are unordered.
- Indexing is not allowed.
- Searching in a set is very fast.

Example:

```python
numbers = {1, 2, 3, 3, 4}

print(numbers)
```

Output

```
{1,2,3,4}
```

---

## 4. Set Operations

### Union

Combines all unique elements.

```python
A | B
```

or

```python
A.union(B)
```

---

### Intersection

Returns common elements.

```python
A & B
```

or

```python
A.intersection(B)
```

---

### Difference

Returns elements present in one set but not the other.

```python
A - B
```

or

```python
A.difference(B)
```

---

### Symmetric Difference

Returns elements present in either set but not both.

```python
A ^ B
```

or

```python
A.symmetric_difference(B)
```

---

## 5. Tuples vs Lists vs Sets

| Feature | Tuple | List | Set |
|----------|--------|------|-----|
| Ordered | Yes | Yes | No |
| Mutable | No | Yes | Yes |
| Duplicate Values | Yes | Yes | No |
| Indexing | Yes | Yes | No |
| Lookup Speed | Fast | Medium | Fastest |
| Best Use | Fixed Data | Changing Data | Unique Data |

---

# Practical Tasks

## Task 1: Geographic Coordinates System

### What I Implemented

- Stored city coordinates using tuples.
- Calculated distance between cities.
- Found the closest city.
- Returned multiple values as tuples.
- Demonstrated tuple immutability.

### Skills Learned

- Tuple creation
- Tuple unpacking
- Mathematical calculations
- Returning tuples from functions

---

## Task 2: Unique Visitor Tracker

### What I Implemented

- Stored website visitor IP addresses in sets.
- Automatically removed duplicate visitors.
- Compared visitors across different days.
- Found:
  - Common visitors
  - New visitors
  - Visitors who left
  - Total unique visitors

### Skills Learned

- Union
- Intersection
- Difference
- Symmetric Difference
- Set membership testing

---

## Task 3: Email Validation System

### What I Implemented

- Maintained a set of valid email domains.
- Checked whether an email contains the '@' symbol.
- Verified that the email domain exists in the valid domain set.
- Stored registered email addresses in a set to prevent duplicates.
- Found emails belonging to a specific domain.

### Skills Learned

- String splitting
- Membership operator (`in`)
- Sets for duplicate prevention
- Basic email validation

---

# Challenges Faced

- Understanding tuple unpacking.
- Learning when to use tuples instead of lists.
- Understanding why sets do not maintain insertion order.
- Learning different set operations.
- Validating email domains using string splitting.

---

# Key Takeaways

- Tuples are immutable and ideal for fixed data.
- Lists are suitable when data changes frequently.
- Sets automatically remove duplicates.
- Set operations make comparing collections simple.
- Tuples can return multiple values from functions.
- Sets provide very fast membership checking.
- Email validation becomes easier by combining strings and sets.

---

# References

### AI Tools
- ChatGPT
- Google Gemini
- Claude AI

### Article
- Python Official Documentation:
  https://docs.python.org/3/tutorial/datastructures.html

---

# Self Reflection

Today I gained a clear understanding of tuples and sets. I learned how tuples protect fixed data from modification and how sets simplify handling unique values. Through the practical tasks, I improved my ability to solve real-world problems using tuple unpacking, distance calculations, email validation, and set operations. I also became more confident in deciding when to use tuples, lists, or sets depending on the problem.
