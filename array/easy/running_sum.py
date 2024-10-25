import sys
from array import array

# O(n) complexity
def get_running_sum(nums):
    arr_len = len(nums)
    if arr_len <= 1:
        return nums

    result = [0] * arr_len
    result[0] = nums[0]
    # memory_used = sys.getsizeof(result)
    # result = [nums[0]] * arr_len - will it make any diff?

    for i in range(1, arr_len):
        result[i] = result[i-1] + nums[i]

    return result

# O(n) complexity
# uses less memory but not suitable for big numbers?
def get_running_sum2(nums):
    arr_len = len(nums)
    if arr_len <= 1:
        return nums
    result = array('i', [0] * arr_len)
    result[0] = nums[0]
    # memory_used = sys.getsizeof(result)

    for i in range(1, arr_len):
        result[i] = result[i-1] + nums[i]

    return result


# input_data = [1,2,3,4]
# input_data = [1,1,1,1,1]
input_data = [3,1,2,10,1, 5, 6, 7, 8, 9, 3, 42343, 7, 15]
# input_data = []
# input_data = [5]
# input_data = [-5, 4, 6]
running_sum = get_running_sum(input_data)

