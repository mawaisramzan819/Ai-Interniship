import math

# Day 12 - Task 1: Math Utility Library

def calculate_average(data, precision=2):
    """
    Calculates the arithmetic average of a list of numbers.

    Parameters:
        data (list): A list of integers or floats. Example: [10, 20, 30]
        precision (int): Number of decimal places to round to. Default: 2

    Returns:
        float: The average value rounded to specified precision.

    Example:
        >>> calculate_average([85, 90, 78, 92, 88])
        86.6
    """
    if len(data) == 0:
        print("Error! Your data is empty.")
        return None

    for item in data:
        if not isinstance(item, (int, float)):
            print("You entered wrong information!")
            return None

    average = sum(data) / len(data)
    return round(average, precision)


def find_median(data, precision=2):
    """
    Finds the median (middle value) of a dataset.

    Parameters:
        data (list): A list of integers or floats. Example: [10, 20, 30, 40]
        precision (int): Number of decimal places to round to. Default: 2

    Returns:
        float: The median value rounded to specified precision.

    Example:
        >>> find_median([3, 7, 12, 19, 45])
        12.0
        >>> find_median([3, 7, 12, 19])
        9.5
    """
    if len(data) == 0:
        print("Error! Your data is empty.")
        return None

    for item in data:
        if not isinstance(item, (int, float)):
            print("You entered wrong information!")
            return None

    sorted_data = sorted(data)
    N = len(sorted_data)
    mid = N // 2

    if not N % 2 == 0:
        return round(sorted_data[mid], precision)
    else:
        return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, precision)


def get_standard_deviation(data, precision=2):
    """
    Calculates the population standard deviation of a dataset.

    Parameters:
        data (list): A list of integers or floats. Example: [10, 20, 30]
        precision (int): Number of decimal places to round to. Default: 2

    Returns:
        float: The standard deviation value rounded to specified precision.

    Example:
        >>> get_standard_deviation([10, 20, 30])
        8.16
    """
    if len(data) == 0:
        print("Error! Your data is empty.")
        return None

    for item in data:
        if not isinstance(item, (int, float)):
            print("You entered wrong information!")
            return None

    mean = sum(data) / len(data)
    square_diff = []
    for x in data:
        result = (x - mean) ** 2
        square_diff.append(result)
    variance = sum(square_diff) / len(data)

    standard_deviation = math.sqrt(variance)
    return round(standard_deviation, precision)


if __name__ == "__main__":
    print("=== DAY 12: MATH UTILITY LIBRARY ===\n")

    # Get user input
    raw = input("Enter numbers separated by commas (e.g. 10,20,30): ")
    numbers = []

    for item in raw.split(","):
        try:
            numbers.append(float(item.strip()))
        except ValueError:
            print(f"'{item.strip()}' is not valid! Skipping.")

    if numbers:
        print(f"\nYour numbers: {numbers}")
        print(f"Average: {calculate_average(numbers)}")
        print(f"Median: {find_median(numbers)}")
        print(f"Standard Deviation: {get_standard_deviation(numbers)}")
    else:
        print("No valid numbers entered!")
