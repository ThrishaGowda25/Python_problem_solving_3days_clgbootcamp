text = input()
words = text.split()
articles = ["a", "an", "the"]
result = []
for word in words:
    if word.lower() not in articles:
        result.append(word)
print(" ".join(result))
