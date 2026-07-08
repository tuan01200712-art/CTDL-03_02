def group_by_first_letter(words):
    groups = {}

    for word in words:
        key = word[0]

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return groups


words = ["apple", "ant", "banana", "ball", "cat"]

result = group_by_first_letter(words)

print(result)