import random

name = input("WHats is your name?")
print("GOOD LUCK!!!!!!", name)

words = ['rainbow', 'water', 'computer', 'science', 'programming', 'python', 'board', 'geeks']
word = random.choice(words)

print("guesssssssssssssssssssssssssssssssssss")

guesses = ''
turns = 12

while turns > 0: 

    failed = 0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("you winnn")
        print("the word is ", word)
        break


    print()
    guess = input("guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("WRONG")
        print("you have", + turns, "more guesses")


        if turns == 0:
            print("PERDEEEEEEEEEEEEEEEEEEEEEEEEEU")
        
