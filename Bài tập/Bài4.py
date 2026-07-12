def dailyTemperatures(T):
    result = [0] * len(T)
    stack = []

    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            index = stack.pop()
            result[index] = i - index

        stack.append(i)

    return result


T = [73, 74, 75, 71, 69, 72, 76, 73]

print("Nhiệt độ:", T)
print("Kết quả :", dailyTemperatures(T))
