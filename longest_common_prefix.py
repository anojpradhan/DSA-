def longest_common_prefix(words):
    if not words:
        return ""

    for i in range(len(words[0])):
        char = words[0][i]
        for word in words[1:]:
            if i >= len(word) or word[i] != char:
                return words[0][:i]

    return words[0]


print(longest_common_prefix(["flower", "flow", "flight"]))
