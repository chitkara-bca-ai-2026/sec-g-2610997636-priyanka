print("==================================================")
print("              TEXT PROCESSING TOOL                ")
print("==================================================")

sentence =input("Enter a sentence: ")
print("\n--- Processing Results ---")

position = int(input("Enter position for indexing: "))
print("Character at position", position, ":", "'" + sentence[position] + "'")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing : "))
sliced_string = sentence[start:end]

print("Sliced string [" + str(start) + ":" + str(end) + "]       :", "'" + sliced_string + "'")

uppercase = sentence.upper()
lowercase = sentence.lower()

print("Uppercase                         :", uppercase)
print("Lowercase                         :", lowercase)

old_word = input("Enter word to replace            : ")
new_word = input("Enter replacement word           : ")

replaced = sentence.replace(old_word, new_word)

print("After replace                     :", replaced)

length = len(sentence)

print("Length of sentence                :", length)

print("\n=================================================")
print("Analysis Complete!")
print("==================================================")


