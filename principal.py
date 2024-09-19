import matplotlib.pyplot as plt
import matplotlib.patches as patches

def gerar_tabela_binaria(n):
    max_num = 2**n
    tabela = []
    for i in range(max_num):
        binario = format(i, f'0{n}b')  # Formata o número i em binário com n dígitos
        tabela.append([int(b) for b in binario])
    return tabela

# Função para calcular os movimentos baseado na tabela binária
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
    ax.add_patch(patches.Rectangle((1 - haste_largura / 2, 0), haste_largura, haste_altura, edgecolor='black', facecolor='grey'))
    ax.add_patch(patches.Rectangle((3 - haste_largura / 2, 0), haste_largura, haste_altura, edgecolor='black', facecolor='grey'))
    ax.add_patch(patches.Rectangle((5 - haste_largura / 2, 0), haste_largura, haste_altura, edgecolor='black', facecolor='grey'))

    cores = plt.cm.rainbow_r(range(n))
    for disco in range(1, n + 1):
        posicao = posicoes[disco]
        largura_disco = 0.6 * (n - disco + 1)  
        centro_x = (posicao * 2) - 1  
        ax.add_patch(patches.Rectangle((centro_x - largura_disco / 2, disco - 0.5), largura_disco, 0.5, facecolor=cores[disco - 1], edgecolor='black'))

    
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
        
        if disco % 2 == 1: 
            if posicoes[disco] == 1:  
                nova_posicao = 3 
            elif posicoes[disco] == 3:  
                nova_posicao = 2  
            else:
                nova_posicao = 1  
        else:  
            if posicoes[disco] == 1:
                nova_posicao = 2  
            elif posicoes[disco] == 2:
                nova_posicao = 3  
            else:
                nova_posicao = 1
        
        posicoes[disco] = nova_posicao

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
