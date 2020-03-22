#reverse each word

sentence = input("enter your sentence:   ")
lst = sentence.split()
output = ""
for word in lst:
    rev = word[::-1]
    output += rev + " "
print(output)
