"""
Day 11 - Task 2: Pattern Generators & Matrix Operations
Xeven Solutions AI Engineer Internship

This script demonstrates nested loops in Python:
1. Multiplication Table Generator
2. Number Triangles & Pyramid Patterns
3. Matrix Operations (Transpose, Row/Column Sums, Diagonals)
4. ASCII Art Generator using Nested Loops and Conditionals
"""

def generate_multiplication_table(size: int = 5) -> None:
    """Generates a formatted multiplication table using nested for loops."""
    print("=" * 45)
    print(f"1. MULTIPLICATION TABLE (1 to {size})")
    print("=" * 45)
    
    # Outer loop controls the rows (multiplicand)
    for row in range(1, size + 1):
        # Inner loop controls the columns (multiplier)
        for col in range(1, size + 1):
            product = row * col
            # print with end="\t" keeps items on the same line with tab spacing
            print(f"{row}x{col}={product:2d}", end="\t")
        # Print an empty line to move to the next row
        print()
    print()


def generate_number_triangle(rows: int = 5) -> None:
    """Generates a number triangle pattern using nested loops."""
    print("=" * 45)
    print("2. NUMBER TRIANGLE PATTERN")
    print("=" * 45)
    
    # Outer loop for number of rows
    for i in range(1, rows + 1):
        # Inner loop prints the number 'i', 'i' times
        for _ in range(i):
            print(i, end=" ")
        print()
    print()


def generate_pyramid(rows: int = 5) -> None:
    """Generates a centered star pyramid using nested loops."""
    print("=" * 45)
    print("3. STAR PYRAMID PATTERN")
    print("=" * 45)
    
    for i in range(1, rows + 1):
        # Print leading spaces for alignment
        for _ in range(rows - i):
            print(" ", end="")
        # Print stars (2*i - 1 stars per row)
        for _ in range(2 * i - 1):
            print("*", end="")
        print()
    print()


def matrix_operations() -> None:
    """Demonstrates matrix operations using nested loops."""
    print("=" * 45)
    print("4. MATRIX OPERATIONS")
    print("=" * 45)
    
    # 3x3 Matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    print("Original Matrix:")
    for row in matrix:
        print(row)
        
    # A. Matrix Transpose (swap rows and columns)
    transpose = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transpose.append(new_row)
        
    print("\nTransposed Matrix (Rows <-> Columns):")
    for row in transpose:
        print(row)
        
    # B. Row Sums & Column Sums
    print("\nRow Sums:")
    for r in range(rows):
        row_sum = 0
        for c in range(cols):
            row_sum += matrix[r][c]
        print(f"Row {r + 1} Sum: {row_sum}")
        
    # C. Diagonal Elements (Primary Diagonal where r == c)
    diagonal = []
    for r in range(rows):
        for c in range(cols):
            if r == c:
                diagonal.append(matrix[r][c])
    print(f"\nMain Diagonal Elements: {diagonal}")
    print()


def generate_ascii_art_box(size: int = 6) -> None:
    """Generates a hollow square ASCII art using nested loops and conditionals."""
    print("=" * 45)
    print("5. ASCII ART GENERATOR (HOLLOW BOX)")
    print("=" * 45)
    
    for r in range(size):
        for c in range(size):
            # Print '*' if on boundary (first/last row OR first/last column)
            if r == 0 or r == size - 1 or c == 0 or c == size - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
    print()


if __name__ == "__main__":
    print("=== DAY 11: PATTERN GENERATORS & MATRIX OPERATIONS DEMO ===\n")
    generate_multiplication_table(5)
    generate_number_triangle(5)
    generate_pyramid(5)
    matrix_operations()
    generate_ascii_art_box(6)
