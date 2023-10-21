from random import randint

def apresentacao():
    print(20 * "*")
    print("Jogo da forca")
    print(20 * "*")

def gerador_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    num = randint(0, len(palavras))
    return palavras[num].upper()

def acertos_letra(pal_sec, chute, let_cert):
    index = 0
    for letra in pal_sec:
        if chute == letra:
            let_cert[index] = letra
        index += 1

def mensagem_vencedor(palavra):
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra):
    print("\nPuxa, você foi enforcado!")
    print(f"A palavra era {palavra}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    apresentacao()

    pal_sec = gerador_palavras()

    let_cert = ["_" for letra in pal_sec]
    print(let_cert)

    erros = 0
    enforcado = False
    acertou = False

    while not enforcado and not acertou:

        chute = input("Palavra: ").strip().upper()

        if chute in pal_sec:
            acertos_letra(pal_sec, chute, let_cert)
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {7-erros} tentativas\n")
            desenho_forca(erros)
        
        enforcado = erros == 7
        acertou = "_" not in let_cert
        print(let_cert)

    if acertou:
        mensagem_vencedor(pal_sec)
    else:
        mensagem_perdedor(pal_sec)

if __name__ == "__main__":
    jogar()