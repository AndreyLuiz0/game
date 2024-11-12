
def mostrar_scenario(fase):
    if fase == 1:
        print("\nVocê está em uma sala. Você vê um baú fechado e uma porta trancada.")
    elif fase == 2:
        print("\nVocê está em uma caverna escura. Você vê uma tocha apagada e uma passagem estreita.")
    elif fase == 3:
        print("\nVocê está em um jardim. Você vê uma fonte e um portão trancado.")
    print("O que você quer fazer?")
    print("1 - Examinar o ambiente")
    print("2 - Interagir com um objeto")
    print("3 - Verificar inventário")

def examinar_ambiente(fase, inventario):
    if fase == 1:
        if "chave" not in inventario:
            print("\nVocê examina o baú e encontra uma chave dentro dele!")
            inventario.append("chave")
        else:
            print("\nO baú já foi examinado e não tem mais nada.")
    elif fase == 2:
        if "tocha" not in inventario:
            print("\nVocê encontra uma tocha apagada no chão.")
            inventario.append("tocha")
        else:
            print("\nNão há mais nada na caverna.")
    elif fase == 3:
        if "chave do portão" not in inventario:
            print("\nVocê encontra uma chave do portão escondida na fonte.")
            inventario.append("chave do portão")
        else:
            print("\nNão há mais nada no jardim.")

def interagir_objeto(fase, inventario):
    if fase == 1:
        if "chave" in inventario:
            print("\nVocê usa a chave para abrir a porta e escapar!")
            return True, 2  # O jogador avança para a próxima fase
        else:
            print("\nA porta está trancada. Você precisa de uma chave para abri-la.")
    elif fase == 2:
        if "tocha" in inventario:
            print("\nVocê acende a tocha e encontra uma passagem secreta que leva ao jardim!")
            return True, 3  # O jogador avança para a próxima fase
        else:
            print("\nEstá muito escuro para ver qualquer coisa. Você precisa de uma tocha.")
    elif fase == 3:
        if "chave do portão" in inventario:
            print("\nVocê usa a chave do portão para abrir o portão e escapar!")
            return True, 0  # O jogador ganhou o jogo
        else:
            print("\nO portão está trancado. Você precisa de uma chave para abri-lo.")
    return False, fase

def jogo():
    inventario = []
    fase = 1
    jogo_ativo = True

    while jogo_ativo:
        mostrar_scenario(fase)

        # Entrada do jogador
        escolha = input("Escolha uma ação (1/2/3): ")

        if escolha == "1":
            examinar_ambiente(fase, inventario)
        elif escolha == "2":
            ganhou, nova_fase = interagir_objeto(fase, inventario)
            if ganhou:
                if nova_fase == 0:
                    print("Parabéns, você escapou!")
                    jogo_ativo = False
                else:
                    fase = nova_fase
        elif escolha == "3":
            if inventario:
                print("\nSeu inventário: ", inventario)
            else:
                print("\nSeu inventário está vazio.")
        else:
            print("\nEscolha inválida. Tente novamente.")

# Inicia o jogo
jogo()
