import matplotlib.pyplot as plt
import matplotlib.patches as patches

def gerar_tabela_binaria(n):
    max_num = 2**n
    tabela = []
    for i in range(max_num):
        binario = format(i, f'0{n}b')  # Formata o número i em binário com n dígitos
        tabela.append([int(b) for b in binario])
    return tabela

def movimentos_pela_tabela_binaria(tabela, n):
    movimentos = []
    
    for i in range(1, len(tabela)):
        for disco in range(n):
            if tabela[i-1][disco] == 0 and tabela[i][disco] == 1:
                movimentos.append((disco + 1, i)) 
    return movimentos

# Função para desenhar as hastes e os discos em cada movimento
def desenhar_torres(posicoes, n, movimento_atual, movimento_texto=""):
    fig, ax = plt.subplots()

    haste_largura = 0.1  # Hastes finas
    altura_disco = 0.1   # Ajuste feito aqui: altura menor para os discos

    # Altura das hastes ajustada para que elas fiquem adequadas ao número de discos
    haste_altura = n * altura_disco + 0.5  # Pequena margem no topo

    # Desenhar as hastes
    ax.add_patch(patches.Rectangle((1 - haste_largura / 2, 0), haste_largura, haste_altura, edgecolor='black', facecolor='grey'))
    ax.add_patch(patches.Rectangle((3 - haste_largura / 2, 0), haste_largura, haste_altura, edgecolor='black', facecolor='grey'))
    ax.add_patch(patches.Rectangle((5 - haste_largura / 2, 0), haste_largura, haste_altura, edgecolor='black', facecolor='grey'))

    cores = plt.cm.rainbow_r(range(n))

    # Contadores de altura para cada haste
    altura_nas_hastes = {1: 0, 2: 0, 3: 0}

    # Desenhar os discos
    for disco in range(1, n + 1):
        posicao = posicoes[disco]
        altura_nas_hastes[posicao] += 1  # Aumentar a altura para o próximo disco nessa haste
        
        largura_disco = 0.3 * (n - disco + 1)  # Discos menores em largura
        centro_x = (posicao * 2) - 1  # Calcular a posição horizontal da haste
        altura_disco_atual = (altura_nas_hastes[posicao] - 1) * altura_disco  # Calcular altura para empilhar sem espaçamento

        # Desenhar o disco com a nova largura e altura
        ax.add_patch(patches.Rectangle((centro_x - largura_disco / 2, altura_disco_atual), largura_disco, altura_disco, facecolor=cores[disco - 1], edgecolor='black'))

    ax.set_xlim(0, 6)
    ax.set_ylim(0, haste_altura)
    ax.set_xticks([1, 3, 5])
    ax.set_xticklabels(['A', 'B', 'C'])
    ax.set_yticks([])

    ax.set_title(f"Movimento {movimento_atual}: {movimento_texto}")
    
    plt.show()

def determinar_hastes_grafico(n, origem, destino, auxiliar, movimentos):
    posicoes = {i: 1 for i in range(1, n+1)}  # Todos os discos começam na haste A (1)

    desenhar_torres(posicoes, n, 0, "Início")  # Desenhar o estado inicial

    for movimento_atual, (disco, _) in enumerate(movimentos, 1):
        haste_atual = posicoes[disco]

        if disco % 2 == 1:  # Discos ímpares seguem uma sequência diferente
            if posicoes[disco] == 1:  # Se o disco está na haste 1 (A)
                nova_posicao = 3  # Vai para a haste 3 (C)
            elif posicoes[disco] == 3:  # Se está na haste 3 (C)
                nova_posicao = 2  # Vai para a haste 2 (B)
            else:
                nova_posicao = 1  # Vai para a haste 1 (A)
        else:  # Discos pares seguem a sequência oposta
            if posicoes[disco] == 1:
                nova_posicao = 2  # Vai para a haste 2 (B)
            elif posicoes[disco] == 2:
                nova_posicao = 3  # Vai para a haste 3 (C)
            else:
                nova_posicao = 1  # Vai para a haste 1 (A)

        # Definir o texto do movimento
        torres = {1: 'A', 2: 'B', 3: 'C'}
        movimento_texto = f"Mover disco {disco} da torre {torres[haste_atual]} para a torre {torres[nova_posicao]}"

        posicoes[disco] = nova_posicao  # Atualizar a posição do disco

        desenhar_torres(posicoes, n, movimento_atual, movimento_texto)  # Desenhar o estado atual com o texto do movimento

def mostrar_solucao_com_grafico(n):
    # Gerar a tabela binária
    tabela = gerar_tabela_binaria(n)

    print(f"Gerando gráfico para {n} discos...\n")
    
    movimentos = movimentos_pela_tabela_binaria(tabela, n)

    origem = 'a'
    destino = 'c'
    auxiliar = 'b'

    determinar_hastes_grafico(n, origem, destino, auxiliar, movimentos)

def main():
    n = int(input("Quantos discos são? "))
    mostrar_solucao_com_grafico(n)

# Chamada da função principal
if __name__ == "__main__":
    main()
