def mostrar_scenario(fase):
    if fase == 1:
        print("\n Ao acordar, você se encontra em uma sala desconhecida, com paredes de pedra fria e um leve cheiro de mofo no ar. Ao seu redor, há apenas um baú fechado e uma porta trancada. Você se levanta, lembrando-se das palavras dos líderes em seu sonho.Qual proxima ação?")
    elif fase == 2:
        print("\n O corredor leva a uma caverna escura e úmida.")
    elif fase == 3:
        print("\n A passagem secreta leva a um jardim encantado, cheio de flores exóticas e uma fonte cristalina. No centro do jardim, há um portão trancado.")
    print("O que você quer fazer?")
    print("1 - vasculhar tudo no ambiente")
    print("2 - Usar oque eu achei")
    print("3 - Ver o que tenho no meu inventário")

def examinar_ambiente(fase, inventario):
    if fase == 1:
        if "chave" not in inventario:
            print("\nVocê decide examinar o baú e, para sua surpresa, encontra uma chave dentro dele.")
            inventario.append("chave")
        else:
            print("\nO baú já foi examinado e não tem mais nada.")
    elif fase == 2:
        if "tocha" not in inventario:
            print("\n Ao meio de diversas pedras insetos e a muita escuridão de repente no chão, você encontra uma tocha apagada.")
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
            print("Ao girar a chave na fechadura, a porta se abre com um rangido, revelando um corredor escuro à sua frente. Você avança com cautela, sentindo a adrenalina correr em suas veias.")
            return True, 2  # O jogador avança para a próxima fase
        else:
            print("\nA porta está trancada. Você precisa de uma chave para abri-la.")
    elif fase == 2:
        if "tocha" in  inventario:
            print("\nvocê pega a tocha e a acende, iluminando o caminho à sua frente. A luz revela uma passagem estreita que você decide seguir. A cada passo, o som de gotas de água ecoa pelas paredes da caverna, criando uma atmosfera tensa.")
            return True, 3  # O jogador avança para a próxima fase
        else:
            print("\nEstá muito escuro para ver qualquer coisa. Você precisa de uma tocha")
    elif fase == 3:
        if "chave do portão" in inventario:
            print("\nCom a chave em mãos, você se aproxima do portão e o destranca, revelando um caminho que leva a um novo mundo cheio de aventuras.")
            return True, 4  # O jogador completa o jogo
        else:
            print("\nO portão está trancado. Você precisa da chave do portão para abri-lo.")
    return False, fase  # O jogador não avança de fase

# Exemplo de uso
fase_atual = 1
inventario = []

while fase_atual <= 3:
    mostrar_scenario(fase_atual)
    acao = int(input("Escolha uma ação: "))
    if acao == 1:
        examinar_ambiente(fase_atual, inventario)
    elif acao == 2:
        avancar, nova_fase = interagir_objeto(fase_atual, inventario)
        if avancar:
            fase_atual = nova_fase
    elif acao == 3:
        print("\nInventário:", inventario)
    else:
        print("\nAção inválida. Tente novamente.")
