# Problem 5: Word frequency counter

sentence = "Hello, world! Hello again.".strip().lower()

for char in ",.!?;:":
    sentence = sentence.replace(char, "")

words_list = sentence.split()
freq_dict = {}

for word in words_list:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

most_common_word = max(freq_dict, key=freq_dict.get)

print("Words list:", words_list)
print("Frequencies:", freq_dict)
print("Most common word:", most_common_word)
