mytext = "data structures and algorithms"
frequenyDictionary = {}

for char in mytext:
    if char in frequenyDictionary:
        frequenyDictionary[char] += 1
    else:
        frequenyDictionary[char] = 1

print(frequenyDictionary)
