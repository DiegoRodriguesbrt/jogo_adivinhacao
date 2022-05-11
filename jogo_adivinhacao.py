import random


def mensagem_abertura():
    print("\n*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")
    print("\n")

def mensagem_termino():
    print("\nFim do jogo!!")
    print("*************************************")
    print("Jogo feito por Diego Rodrigues - 2022")
    print("*************************************")

def jogar():

    mensagem_abertura()

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 100
    numero_tentativas = 0

    while total_de_tentativas > 0:

        total_de_tentativas -= 1
        numero_tentativas += 1
        print("** Tentativa número {} **".format(numero_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Digite um número válido!! \n")
            continue

        acertou = (numero_secreto == chute)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("\nVocê acertou e ganhou o jogo, PARABÉNS :D")
            print("Você precisou de {} tentativa(s) para acertar!!".format(numero_tentativas))
            break

        else:
            if (maior):
                print("Você errou, o seu chute ({}) foi maior que o número secreto :( \n\n\n\n".format(chute))

            elif (menor):
                print("Você errou, o seu chute ({}) foi menor que o número secreto :( \n\n\n\n".format(chute))

    mensagem_termino()


if (__name__ == "__main__"):
    jogar()
