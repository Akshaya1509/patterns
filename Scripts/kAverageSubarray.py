from __future__ import division

def kAverageSubarray(arr, k):
    if k == 0:
        return
    prev, next_val, index = 0, 0, 0
    avg = []
    arr_sum = sum(arr[:index + k])
    upper_limit = len(arr) - k
    while index <= upper_limit:
        arr_sum = arr_sum - prev + next_val
        avg.append(arr_sum / k)
        prev = arr[index]
        next_val =  arr[index + k] if index < upper_limit  else 0
        index += 1
    return avg

def main():
    arr = [1, 3, 2, 6, -1 ,4, 1, 8, 2]
    k = 5
    print(kAverageSubarray(arr, k))
    # arr = [1, 2, 3, 4, 5]
    # k = 2
    # print(kAverageSubarray(arr, k))
    arr = []
    k = 0
    print(kAverageSubarray(arr, k))

main()