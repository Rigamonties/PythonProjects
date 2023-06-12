print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

n_secreto = 17

adivinhe_str = input("Digite o seu número: ")
print("Você digitou: ", adivinhe_str)
chute = int(adivinhe_str)

acertou = chute == n_secreto
maior = chute > n_secreto
menor = chute < n_secreto

if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu número foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu número foi menor que o número secreto.")