"""
PROBLEM 1 (Hard)
Prompt:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
"""

from typing import List


def problem_1_llama3_1_70B():
    """
    Here is a solution using binary search to achieve the required time complexity of O(log (m+n)).
    This solution uses binary search to find the median of the two sorted arrays. The basic idea is to partition the two arrays into two parts each, such that the elements on the left side of the partition are smaller than the elements on the right side.
    We start by ensuring that nums1 is the smaller array. We then calculate the total length of both arrays and the half length.
    We initialize the binary search range to be the entire range of nums1. We then enter a loop where we calculate the partition point for nums1 and nums2 based on the current binary search range.
    We calculate the values at the partition points and check if the partition is correct. If the partition is correct, we return the median. If the partition is not correct, we adjust the binary search range and repeat the process.

    Time Complexity
    The time complexity of this solution is O(log (m+n)), where m and n are the lengths of the two arrays. This is because we use binary search to find the median, and the number of iterations is proportional to the logarithm of the total length of the two arrays.

    Space Complexity
    The space complexity of this solution is O(1), as we only use a constant amount of space to store the partition points and the values at the partition points.
    """

    class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            # Ensure that nums1 is the smaller array
            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1

            # Calculate the total length of both arrays
            total_length = len(nums1) + len(nums2)

            # If the total length is odd, the median is the middle element
            # If the total length is even, the median is the average of the two middle elements
            half_length = total_length // 2

            # Initialize the binary search range
            left, right = 0, len(nums1) - 1

            while True:
                # Calculate the partition point for nums1
                i = (left + right) // 2

                # Calculate the partition point for nums2
                j = half_length - i - 2

                # Calculate the values at the partition points
                nums1_left = nums1[i] if i >= 0 else float('-infinity')
                nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')
                nums2_left = nums2[j] if j >= 0 else float('-infinity')
                nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')

                # Check if the partition is correct
                if nums1_left <= nums2_right and nums2_left <= nums1_right:
                    # If the total length is odd, return the middle element
                    if total_length % 2:
                        return min(nums1_right, nums2_right)
                    # If the total length is even, return the average of the two middle elements
                    else:
                        return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                # If the partition is not correct, adjust the binary search range
                elif nums1_left > nums2_right:
                    right = i - 1
                else:
                    left = i + 1


def problem_1_gpt4o():
    """
    To solve the problem of finding the median of two sorted arrays nums1 and nums2 in O(log(m + n)) time complexity, we can use a binary search approach. The key idea is to partition the two arrays such that the left half and the right half are balanced, and then use the maximum of the left half and the minimum of the right half to calculate the median.

Steps to Solve:

1. Partition the arrays: We will try to partition the combined array such that the left half contains half of the elements (or one more in case of an odd total number of elements) and the right half contains the other half.


2. Binary Search: We perform a binary search on the smaller of the two arrays. For each partition of the smaller array, we can compute the corresponding partition in the larger array.


3. Ensure valid partitions: The partition is valid if the maximum element of the left half of both arrays is less than or equal to the minimum element of the right half of both arrays. If this condition holds, we can compute the median.


4. Handling even and odd length:

If the combined array has an odd length, the median will be the maximum of the left side.

If the combined array has an even length, the median will be the average of the maximum of the left side and the minimum of the right side.
Explanation of Code:

1. Binary Search on Smaller Array: We always perform binary search on the smaller array (nums1), which helps to ensure that we minimize the number of operations.


2. Partition Calculation: The partition in nums2 is calculated based on the partition in nums1 such that the total number of elements in the left partition of both arrays combined is half the total number of elements.


3. Checking Valid Partition: We check if the maximum element on the left side of the partition is less than or equal to the minimum element on the right side. If this condition is met, the partition is correct.


4. Edge Case Handling: If the partition indices reach the bounds of either array, we use -inf or inf as substitutes for missing elements to handle edge cases.


5. Return the Median:

If the total number of elements is odd, the median is the maximum element from the left half.

If the total number of elements is even, the median is the average of the largest element from the left half and the smallest element from the right half.




Time Complexity:

The time complexity is O(log(min(m, n))) because we are performing a binary search on the smaller array.
    :return:
    """

    class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            # Ensure nums1 is the smaller array
            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1

            m, n = len(nums1), len(nums2)
            total_len = m + n
            half_len = (total_len + 1) // 2

            left, right = 0, m

            while left <= right:
                i = (left + right) // 2
                j = half_len - i

                # Edge cases where i == 0 or i == m
                nums1_left = float('-inf') if i == 0 else nums1[i - 1]
                nums1_right = float('inf') if i == m else nums1[i]

                # Edge cases where j == 0 or j == n
                nums2_left = float('-inf') if j == 0 else nums2[j - 1]
                nums2_right = float('inf') if j == n else nums2[j]

                # Check if we have found the correct partition
                if nums1_left <= nums2_right and nums2_left <= nums1_right:
                    # If the total length is odd, the median is the max of the left side
                    if total_len % 2 == 1:
                        return max(nums1_left, nums2_left)
                    # If the total length is even, the median is the average of the middle two
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                # Adjust search range
                elif nums1_left > nums2_right:
                    right = i - 1
                else:
                    left = i + 1

"""
Here is a coding problem:
***
 Solution 1:
***
 Solution 2:
***
Analyze these solutions. Explain which solution is better.

Llama3.1_70B:
---
Analysis of Solutions Both solutions aim to find the median of two sorted arrays using a binary search approach. They share similar ideas, but there are some differences in implementation details. Solution 1

    The solution uses a while loop to perform binary search.
    It calculates the partition points for both arrays using the formula i = (left + right) // 2 and j = half_length - i - 2.
    It checks if the partition is correct by comparing the values at the partition points.
    If the partition is correct, it returns the median based on whether the total length is odd or even.

Solution 2

    The solution also uses a while loop to perform binary search.
    It calculates the partition points for both arrays using the formula i = (left + right) // 2 and j = half_len - i.
    It checks if the partition is correct by comparing the values at the partition points.
    If the partition is correct, it returns the median based on whether the total length is odd or even.

Comparison of Solutions Both solutions have a time complexity of O(log (m+n)), where m and n are the lengths of the input arrays. However, there are some differences in implementation details that make Solution 2 slightly better:

    Simpler calculation of partition points: Solution 2 uses a simpler formula to calculate the partition points, which reduces the chance of errors.
    Fewer edge cases: Solution 2 handles edge cases (e.g., i == 0 or i == m) more elegantly, using float('-inf') and float('inf') to represent negative and positive infinity, respectively.
    More concise code: Solution 2 has fewer lines of code and is more concise, making it easier to read and understand.

Conclusion Both solutions are correct and efficient, but Solution 2 is slightly better due to its simpler calculation of partition points, fewer edge cases, and more concise code. Therefore, Solution 2 is the preferred solution.

ChatGPT:
Both Solution 1 and Solution 2 aim to solve the problem of finding the median of two sorted arrays in an optimal way with a time complexity of , which meets the required time complexity . However, let's analyze and compare the two solutions in terms of clarity, correctness, and performance.

Solution 1:

Overview:

1. This solution ensures that nums1 is the smaller array, which is essential to keep the time complexity in the desired range.


2. The main idea is to perform a binary search on nums1 to find the correct partition between nums1 and nums2 such that the left part contains elements smaller than or equal to the elements in the right part.


3. Once the correct partition is found, the median is calculated depending on whether the combined length of the two arrays is odd or even.



Key Observations:

Binary Search: The search is applied only on nums1 (smaller array), which reduces the time complexity to .

Partitioning Logic: The solution uses the partition points i for nums1 and j for nums2, and compares values at these points to ensure correct partitioning.

Edge Cases: It handles edge cases like when i or j go out of bounds by assigning -∞ or ∞ to avoid errors when comparing extreme values.


Concerns:

Clarity: The partitioning index calculations (i + 1), (j + 1), and so on might be slightly confusing because it can be difficult to reason about the off-by-one index shifts.

Edge case handling: It handles edge cases with some additional complexity using special conditions for out-of-bounds scenarios, which can make it harder to follow.


Solution 2:

Overview:

1. Similar to Solution 1, it ensures that nums1 is the smaller array to keep the binary search efficient.


2. The binary search finds the correct partition between the two arrays such that the left half contains smaller or equal values compared to the right half.


3. The difference here is that it uses a simplified approach to calculate the partition indices and checks.



Key Observations:

Simplicity: Solution 2 simplifies the logic for handling edge cases by directly checking when i == 0, i == m, j == 0, or j == n to assign -∞ or ∞. This makes the code more readable and easier to understand.

Same Binary Search Complexity: It maintains the same optimal  complexity by performing binary search on the smaller array.

Clearer Partitioning: The partitioning index calculation in Solution 2 is more straightforward than Solution 1, reducing the cognitive overhead when reasoning about the correctness of the solution.


Advantages:

Readability: Solution 2 is more readable and easier to reason about. The partition points are clearer, and handling edge cases is more intuitive.

Efficiency: Both solutions have the same time complexity, but Solution 2 is slightly better in terms of clarity and simplicity, which reduces the chance of implementation errors.


Conclusion:

Correctness: Both solutions are correct and achieve the desired time complexity of .

Readability and Maintainability: Solution 2 is better because it handles edge cases more clearly and has a simpler partitioning logic, which makes it easier to follow.

Performance: Both solutions are similar in terms of performance, but Solution 2 is slightly more elegant and less prone to errors during implementation.


Thus, Solution 2 is preferable due to its better readability and maintainability without sacrificing performance.
"""