words = {}
text = input("Text: ").lower().split()
for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for word, count in words.items():
    print(f"{word:13}: {count}")
