def count_characters(text):
    freq = {}

    # Count alphabetic characters only
    for ch in text.lower():
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    # Return dictionary with keys in alphabetical order
    sorted_freq = {}
    for key in sorted(freq.keys()):
        sorted_freq[key] = freq[key]

    return sorted_freq


# Example
text = "Hello World 123!!"
print(count_characters(text))