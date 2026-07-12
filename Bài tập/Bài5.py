from collections import deque

def slidingWindowMin(A, k):
    dq = deque()
    result = []

    for i in range(len(A)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and A[dq[-1]] > A[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(A[dq[0]])

    return result


A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3

print("Mảng:", A)
print("Kết quả:", slidingWindowMin(A, k))