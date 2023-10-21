from random import randint

def jogar():
    print(20 * "*")
    print("Jogo de adivinhação")
    print(20 * "*")

    num_sec = randint(1, 100)
    tentativas = 0
    pontos = 1000

    print("\nDificuldade do Jogo")
    dif = int(input("(1) Facil (2) Medio (3) Dificil: "))

    if dif == 1:
        tentativas = 20
    elif dif == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f"\nTentativa {rodada} de {tentativas}")
        
        chute = int(input("Digite o chute entre 1 e 100: "))
        print("Você digitou: ", chute)

        if chute < 1 or chute > 100:
            print("Apenas entre 1 e 100")
            continue

        acertou = chute == num_sec
        maior = chute > num_sec
        menor = chute < num_sec

        if acertou:
            print(f"Acertou!!")
            break
        elif maior:
            print("Maior que o numero!!!")
            pontos -= abs(chute - num_sec)
        elif menor:
            print("Menor que o numero!!!")
            pontos -= abs(chute - num_sec)

    print(f"\nNumero secreto = {num_sec}")
    print(f"\nFim de jogo!! {pontos} pontos\n")    

if __name__ == "__main__":
    jogar()