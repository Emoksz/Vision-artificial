# Problem 4: Sentence word statistics
# Description:
# Displays word statistics from a sentence.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Word count
# - First word
# - Last word
# - Shortest word
# - Longest word
#
# Validation:
# - Sentence must not be empty
#
# Test cases:
# 1) Normal: Python is very powerful
# 2) Edge: Hello
# 3) Error: "   "

sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: invalid input")
else:
    words = sentence.split()
    shortest = words[0]
    longest = words[0]

    for w in words:
        if len(w) < len(shortest):
            shortest = w
        if len(w) > len(longest):
            longest = w

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest}")
    print(f"Longest word: {longest}")
