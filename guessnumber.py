import random

print("Ola!, Bem vindo ao Number Guessing Game. \nVocê terá 7 chances de acertar o número.\nVamos começar!")

low = int(input("Seu palpite mais baixo!: "))
high = int(input("Seu palpite mais alto!: "))

print(f"\n Voce tera 7 chances para acertar o numero entre {low} and {high}.\n Vamos Começar!")

num = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("SEU PALPITE?"))

    if guess == num:
        print(f"CORETOOO! O numero correto é {num}. VOCE ADVINHOU EM {gc} TENTATIVAS")
        break
    elif gc >= ch and guess != num:
        print (f"ISH! o numero era {num}. MELHORE A SORTE")

    elif guess > num:
        print("MUITO ALTO, diminue")
    
    elif guess < num:
        print("BAIXO DEMAIS, aumente")