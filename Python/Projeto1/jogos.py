import forca
import adivinhacao

def escolhe_jogos():
    print(20 * "*")
    print("Escolha o jogo")
    print(20 * "*")

    print("(1) Forca (2) Adivinhação")
    esc = int(input("Escolha: "))

    if esc == 1:
        print("\nJogando Forca!\n")
        forca.jogar()
    elif esc == 2:
        print("Jogando adivinhação!\n")
        adivinhacao.jogar()

if __name__ == "__main__":
    escolhe_jogos()