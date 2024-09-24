from typing import Dict, List, Callable
import timeit
import random
import array

# Constants
MIN_YEAR = 1
MAX_YEAR = 50000
NUM_SAMPLES = 5000
ITERATIONS = 10000

# Create a static typed dictionary
year_dict: Dict[str, int] = {str(i): i for i in range(MIN_YEAR, MAX_YEAR + 1)}

# Use array for better memory efficiency and performance
test_years: array.array = array.array('I', random.sample(range(MIN_YEAR, MAX_YEAR + 1), NUM_SAMPLES))
test_strings: List[str] = [str(year) for year in test_years]

def dict_lookup(s: str) -> int:
    """Lookup the integer value in the year_dict by its string key."""
    return year_dict[s]

def int_convert(s: str) -> int:
    """Convert a string to an integer."""
    return int(s)

def time_function(func: Callable[[str], int], input_data: List[str]) -> float:
    """Time the execution of a function over the input data."""
    print("time function called")
    return timeit.timeit(lambda: [func(s) for s in input_data], number=ITERATIONS)

def print_results(dict_time: float, conversion_time: float) -> None:
    """Print the results of the timing tests."""
    print(f"Dictionary lookup time: {dict_time:.7f}")
    print(f"Int conversion time: {conversion_time:.7f}")
    print(f"Dictionary lookup is {conversion_time/dict_time:.2f}x faster")

    dict_avg = dict_time / (NUM_SAMPLES * ITERATIONS)
    int_avg = conversion_time / (NUM_SAMPLES * ITERATIONS)

    print("\nAverage time per operation:")
    print(f"Dictionary lookup: {dict_avg:.9f} seconds")
    print(f"Int conversion: {int_avg:.9f} seconds")

    total_ops = NUM_SAMPLES * ITERATIONS
    print(f"\nTotal operations performed: {total_ops:,}")

if __name__ == "__main__":
    dict_time = time_function(dict_lookup, test_strings)
    conversion_time = time_function(int_convert, test_strings)
    print_results(dict_time, conversion_time)



