"""
Day 11 - Task 3: Number Analysis System
Xeven Solutions AI Engineer Internship

This script implements:
1. Prime Numbers Finder up to N (using while loops)
2. Factorial and Fibonacci Sequence Calculators
3. Interactive Number Guessing Game with hints and attempt limits
"""

import random


def find_primes_up_to_n(limit: int) -> list[int]:
    """Finds all prime numbers up to N using a while loop."""
    primes = []
    num = 2
    
    while num <= limit:
        is_prime = True
        divisor = 2
        # Check divisibility up to square root of num (mathematical optimization)
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
            
        if is_prime:
            primes.append(num)
        num += 1
        
    return primes


def calculate_factorial(n: int) -> int:
    """Calculates n! using an iterative while loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    current = n
    while current > 1:
        result *= current
        current -= 1
    return result


def generate_fibonacci_sequence(count: int) -> list[int]:
    """Generates the first 'count' numbers in the Fibonacci sequence."""
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < count:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence


def number_guessing_game(max_attempts: int = 5) -> None:
    """Interactive number guessing game with attempt limit and hint system."""
    secret = random.randint(1, 100)
    attempt = 1
    
    print("=" * 45)
    print("🎮 NUMBER GUESSING GAME")
    print("I have selected a secret number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
    print("=" * 45)
    
    while attempt <= max_attempts:
        attempts_left = max_attempts - attempt + 1
        print(f"\nAttempt {attempt} of {max_attempts} ({attempts_left} left)")
        
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue
            
        if guess == secret:
            print(f"🎉 BINGO! You guessed the secret number {secret} in {attempt} attempts!")
            return
        elif guess < secret:
            difference = secret - guess
            hint = "Very close! Just a bit higher" if difference <= 5 else "Too low!"
            print(f"📉 {hint}")
        else:
            difference = guess - secret
            hint = "Very close! Just a bit lower" if difference <= 5 else "Too high!"
            print(f"📈 {hint}")
            
        attempt += 1
        
    print(f"\n❌ Game Over! You ran out of attempts. The secret number was {secret}.")


if __name__ == "__main__":
    print("=== DAY 11: NUMBER ANALYSIS SYSTEM ===\n")
    
    # 1. Test Primes
    limit = 30
    primes = find_primes_up_to_n(limit)
    print(f"1. Prime numbers up to {limit}: {primes}\n")
    
    # 2. Test Factorial
    num_fact = 5
    fact_result = calculate_factorial(num_fact)
    print(f"2. Factorial of {num_fact} ({num_fact}!): {fact_result}\n")
    
    # 3. Test Fibonacci
    fib_count = 10
    fib_result = generate_fibonacci_sequence(fib_count)
    print(f"3. First {fib_count} Fibonacci numbers: {fib_result}\n")
