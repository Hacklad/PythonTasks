## Write a program that prompts the user to enter a sentence. Extract all the vowels(unique) from the sentence and store them in a set. Display the set of vowel
vow = ['a','e','i','o','u']
store_set = []
sent = input("Enter your sentence to check: ").lower()
for l in vow:
    if l in sent:
        store_set.append(l)

print(set(store_set))
