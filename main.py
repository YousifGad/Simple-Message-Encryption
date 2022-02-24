from string import ascii_lowercase

mesg = input("Type Your Message: ").lower()
alpha = list(ascii_lowercase)
wordreversed = []

def encrypt(word):
    for letter in word:
        if letter == " ":
            wordreversed.append(letter)

        else:
            index = alpha.index(letter)
            alphareversed = alpha[::-1]
            wordreversed.append(alphareversed[index])

    print("".join(wordreversed))


encrypt(mesg)
