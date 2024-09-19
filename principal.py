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
def desenhar_torres(posicoes, n, movimento_atual):
    fig, ax = plt.subplots()

    haste_largura = 0.2
    haste_altura = n + 1
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
        altura_nas_hastes[posicao] += 1 
        largura_disco = 0.6 * (n - disco + 1)  
        centro_x = (posicao * 2) - 1  
        altura_disco = altura_nas_hastes[posicao] - 0.5  
        ax.add_patch(patches.Rectangle((centro_x - largura_disco / 2, altura_disco), largura_disco, 0.5, facecolor=cores[disco - 1], edgecolor='black'))

    ax.set_xlim(0, 6)
    ax.set_ylim(0, n + 1)
    ax.set_xticks([1, 3, 5])
    ax.set_xticklabels(['A', 'B', 'C'])
    ax.set_yticks([])

    ax.set_title(f"Movimento {movimento_atual}")
    
    plt.show()

def determinar_hastes_grafico(n, origem, destino, auxiliar, movimentos):
    posicoes = {i: 1 for i in range(1, n+1)}  

    desenhar_torres(posicoes, n, 0)  

    for movimento_atual, (disco, _) in enumerate(movimentos, 1):
        if disco % 2 == 1:  # Discos ímpares seguem uma sequência diferente
            if posicoes[disco] == 1:  # Se o disco está na haste 1
                nova_posicao = 3  # Vai para a haste 3
            elif posicoes[disco] == 3:  # Se está na haste 3
                nova_posicao = 2  # Vai para a haste 2
            else:
                nova_posicao = 1  # Vai para a haste 1
        else:  # Discos pares seguem a sequência oposta
            if posicoes[disco] == 1:
                nova_posicao = 2  # Vai para a haste 2
            elif posicoes[disco] == 2:
                nova_posicao = 3  # Vai para a haste 3
            else:
                nova_posicao = 1  # Vai para a haste 1

        posicoes[disco] = nova_posicao  # Atualizar a posição do disco

        desenhar_torres(posicoes, n, movimento_atual)  

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
