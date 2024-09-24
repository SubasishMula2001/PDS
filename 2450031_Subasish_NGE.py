# Logic Overview
# The main idea behind the algorithm is to use a stack to keep track of the elements we are processing and their corresponding indices, enabling us to efficiently find the next greater elements as we iterate through the array.

# Key Concepts:
# Circular Array:

# The array is treated as circular, meaning after reaching the last element, we continue from the first element again. This is achieved by iterating through the array twice (i.e., from 2 * n - 1 to 0), but using the modulus operation (% n) to wrap around.
# Stack for Next Greater Elements:

# The stack helps to maintain a list of elements in decreasing order. When we encounter an element:
# If it’s greater than the top element of the stack, the top element is the Next Greater Element for the current element.
# We pop elements from the stack until we find an element greater than the current one or until the stack is empty.
# Efficient Processing:

# The algorithm effectively processes each element twice (to handle the circular nature), but each element is pushed and popped from the stack at most once. This results in a time complexity that is linear with respect to the number of elements, 
# 𝑂
# (
# 𝑛
# )
# O(n).
# Steps in Logic:
# Initialization:

# Create an empty stack and a results array initialized with -1.
# Iterate Backwards:

# Start iterating from the last element to the first, while effectively considering the circular nature by looping from 2 * n - 1 down to 0.
# Stack Operations:

# For each element:
# While the stack is not empty and the top of the stack is less than or equal to the current element, pop the stack (removing elements that cannot be the NGE for any future elements).
# If the current index is less than n (to avoid writing to an out-of-bounds index), check the stack:
# If the stack is not empty, the top of the stack is the NGE for the current element.
# Push the current element onto the stack.
# Output the Result:

# After processing all elements, the nge array contains the next greater elements for all elements in the original circular array.
# Time Complexity:
# O(n): Each element is pushed and popped from the stack at most once.
# Space Complexity:
# O(n): The stack can hold up to n elements in the worst case, and the output array also requires O(n) space.
# This approach efficiently determines the next greater elements while handling the circular nature of the array using a stack, ensuring optimal performance.

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        st = []


        for i in range(2 * n - 1, -1, -1):
            while st and st[-1] <= nums[i % n]:
                st.pop()


            if i < n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[i % n])
        return nge


if __name__ == '__main__':
    obj = Solution()
    v = [5, 7, 1, 2, 6, 0]
    res = obj.nextGreaterElements(v)
    print("The next greater elements are")
    print(*res)
