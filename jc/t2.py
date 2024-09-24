# This is a potential improvement of the datetime conversion package Pendulum.
# this improvement suggest the use of typed dictionaries instead of type conversion for string representations of date/time components
# such as year, month, etc.
# the improvement was found innitially by asking GPT to improve the packages performance for date conversion by 10%
# although it failed to accomplish the job, it was helpful in finding the potetial area of improvement and then in writing code to isolate that area and generate eveluating code.
# again GPT was not good at evation of the code performce by halucinating the performance results and even by claiming to run/have run the code.
# GPT reported a false eveluation result and provided detailed palusible argumentation to support it.
# then when I ran the code locally and showed the GPY the eveluation result, it changed its mind and provided details argumentation in suport of my results.
# I also found out that the GPT has no undesatanding of best practices for high perfoamce coding, e.g. it did nit suggest static typing.

import timeit
import random
from typing import Dict

# Creating the dictionary

# Increase the range of numbers
num_range = list(range(1, 50001))  # Numbers from 1000 to 5000
num_dict: Dict[str, int] = {str(i): i for i in num_range}

def dict_lookup(s):
    """Lookup the integer value in the num_dict by its string key."""
    return num_dict[s]

def int_convert(s):
    """Convert a string to an integer."""
    return int(s)

test_numbers = random.sample(num_range, 5000)
test_strings = [str(num) for num in test_numbers]

# Increase the number of iterations
iterations = 10000

# Time dictionary lookup
dict_time = timeit.timeit(
    lambda: [dict_lookup(s) for s in test_strings], number=iterations
)

# Time int conversion
int_time = timeit.timeit(
    lambda: [int_convert(s) for s in test_strings], number=iterations
)

print(f"Dictionary lookup time: {dict_time:.7f}")
print(f"Int conversion time: {int_time:.7f}")
print(f"Dictionary lookup is {int_time/dict_time:.2f}x faster")

# Calculate average time per operation
dict_avg = dict_time / (len(test_strings) * iterations)
int_avg = int_time / (len(test_strings) * iterations)

print("\nAverage time per operation:")
print(f"Dictionary lookup: {dict_avg:.9f} seconds")
print(f"Int conversion: {int_avg:.9f} seconds")

# Calculate total operations performed
total_ops = len(test_strings) * iterations
print(f"\nTotal operations performed: {total_ops:,}")