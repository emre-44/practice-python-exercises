from collections import Counter
with open('ex22.txt', 'r') as f:
    words = [line.strip() for line in f.readlines()]

words_count = Counter(words)
for word, count in words_count.items():
    print(f"{word}: {count} times")
