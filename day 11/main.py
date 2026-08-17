"""
Day 11: Loops & Iteration Complete Master Script
Xeven Solutions AI Engineer Internship

This script executes all 3 tasks of Day 11:
- Task 1: Data Processing Pipeline (enumerate, zip, break, continue)
- Task 2: Pattern Generators & Matrix Operations (Nested loops, patterns, matrix ops)
- Task 3: Number Analysis System (Primes, Factorial, Fibonacci, Guessing Game)
"""

from data_pipeline import process_data_pipeline
from pattern_generators import generate_multiplication_table, generate_pyramid, matrix_operations
from number_analysis import find_primes_up_to_n, calculate_factorial, generate_fibonacci_sequence


def main():
    print("=" * 60)
    print("XEVEN SOLUTIONS - DAY 11: LOOPS & ITERATION MASTER DEMO")
    print("=" * 60 + "\n")
    
    # --- TASK 1: DATA PROCESSING PIPELINE ---
    print("\n--- TASK 1: DATA PROCESSING PIPELINE ---")
    process_data_pipeline()
    
    # --- TASK 2: PATTERN GENERATORS & MATRIX OPERATIONS ---
    print("\n--- TASK 2: PATTERN GENERATORS & MATRIX OPERATIONS ---")
    generate_multiplication_table(5)
    generate_pyramid(5)
    matrix_operations()
    
    # --- TASK 3: NUMBER ANALYSIS SYSTEM ---
    print("\n--- TASK 3: NUMBER ANALYSIS SYSTEM ---")
    print("Primes up to 30:", find_primes_up_to_n(30))
    print("5! Factorial:", calculate_factorial(5))
    print("First 10 Fibonacci Numbers:", generate_fibonacci_sequence(10))
    
    print("\n" + "=" * 60)
    print("ALL DAY 11 TASKS EXECUTED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()
