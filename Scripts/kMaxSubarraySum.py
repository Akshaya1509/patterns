def kMaxSubArraySum(arr, k):
    windowSum, windowStart = 0, 0
    max_sum = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            max_sum = max(windowSum, max_sum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return max_sum

def main():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    # arr = [2, 3, 4, 1, 5]
    # k = 2
    print(kMaxSubArraySum(arr, k))

main()