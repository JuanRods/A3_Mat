from typing import Tuple, List

# Constantes para os caracteres de borda
BORDA_SUPERIOR = "╔════════════════════════════════════════╗"
BORDA_INFERIOR = "╚════════════════════════════════════════╝"
BORDA_LATERAL = "║"
BORDA_DIVISORIA = "╠════════════════════════════════════════╣"
BORDA = "════════════════════════════════════════"

def calcular_determinante_3x3(matriz: List[List[float]]) -> float:
    """Calcula o determinante de uma matriz 3x3."""
    return (matriz[0][0] * matriz[1][1] * matriz[2][2] +
            matriz[0][1] * matriz[1][2] * matriz[2][0] +
            matriz[0][2] * matriz[1][0] * matriz[2][1] -
            matriz[0][2] * matriz[1][1] * matriz[2][0] -
            matriz[0][0] * matriz[1][2] * matriz[2][1] -
            matriz[0][1] * matriz[1][0] * matriz[2][2])

def verificar_colinearidade(p1: Tuple[float, float], 
                          p2: Tuple[float, float], 
                          p3: Tuple[float, float]) -> bool:
    """Verifica se três pontos são colineares."""
    matriz = [
        [p1[0], p1[1], 1],
        [p2[0], p2[1], 1],
        [p3[0], p3[1], 1]
    ]
    return calcular_determinante_3x3(matriz) == 0

def calcular_area_triangulo(p1: Tuple[float, float], 
                          p2: Tuple[float, float], 
                          p3: Tuple[float, float]) -> float:
    """Calcula a área de um triângulo formado por três pontos."""
    if verificar_colinearidade(p1, p2, p3):
        return 0.0
    
    det = calcular_determinante_3x3([
        [p1[0], p1[1], 1],
        [p2[0], p2[1], 1],
        [p3[0], p3[1], 1]
    ])
    return abs(det) / 2

def obter_ponto_do_usuario(numero_ponto: int) -> Tuple[float, float]:
    """Solicita ao usuário as coordenadas de um ponto."""
    while True:
        try:
            print(BORDA_SUPERIOR)
            print(f"{BORDA_LATERAL} Digite as coordenadas do ponto {numero_ponto}{' ':>7}{BORDA_LATERAL}")
            print(BORDA_DIVISORIA)
            x = float(input(f"{' ':>12} Coordenada x: "))
            y = float(input(f"{' ':>12} Coordenada y: "))
            print(BORDA_INFERIOR)
            return (x, y)
            
        except ValueError:
            print(BORDA_INFERIOR)
            print("\n" + BORDA_SUPERIOR)
            print(f"{BORDA_LATERAL}ERRO: Digite valores numéricos válidos!{' ':>1}{BORDA_LATERAL}")
            print(BORDA_INFERIOR)

def exibir_resultados(p1: Tuple[float, float], 
                     p2: Tuple[float, float], 
                     p3: Tuple[float, float]):
    """Exibe os resultados formatados com bordas."""
    print(BORDA_SUPERIOR)
    print(f"{BORDA_LATERAL}{' RESULTADOS DO CÁLCULO ':^40}{BORDA_LATERAL}")
    print(BORDA_INFERIOR)
    print(f"{' ':>9} Ponto 1: ({p1[0]:.2f}, {p1[1]:.2f})")
    print(f"{' ':>9} Ponto 2: ({p2[0]:.2f}, {p2[1]:.2f})")
    print(f"{' ':>9} Ponto 3: ({p3[0]:.2f}, {p3[1]:.2f})")
    print(BORDA_SUPERIOR)
    
    area = calcular_area_triangulo(p1, p2, p3)
    if area == 0:
        print(f"{BORDA_LATERAL}{' PONTOS COLINEARES- NÃO FORMAM TRIÂNGULO':^38}{BORDA_LATERAL}")
    else:
        print(f"{'':3} Área do triângulo: {area:.2f} unidades²")
    print(BORDA_INFERIOR)

def menu_principal() -> str:
    """Exibe o menu principal com bordas decorativas."""
    print("\n" + BORDA_SUPERIOR)
    print(f"{BORDA_LATERAL}{' CÁLCULO DE ÁREA DE TRIÂNGULO ':^40}{BORDA_LATERAL}")
    print(BORDA_DIVISORIA)
    print(f"{BORDA_LATERAL} 1 - Usar pontos fixos de exemplo{'':>7}{BORDA_LATERAL}")
    print(f"{BORDA_LATERAL} 2 - Inserir pontos manualmente{' ':>9}{BORDA_LATERAL}")
    print(f"{BORDA_LATERAL} 3 - Sair do programa{' ':>19}{BORDA_LATERAL}")
    print(BORDA_INFERIOR)
    print("\n" + BORDA_SUPERIOR)
    print(f"{BORDA_LATERAL} {' ':8}Digite sua opção (1-3){' ':9}{BORDA_LATERAL}")
    print(BORDA_INFERIOR)
    opcao = input().strip()
    return opcao
    
def main():
    """Função principal do programa."""
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            p1, p2, p3 = (2, 3), (5, 11), (12, 8)
        elif opcao == '2':
            p1 = obter_ponto_do_usuario(1)
            p2 = obter_ponto_do_usuario(2)
            p3 = obter_ponto_do_usuario(3)
        elif opcao == '3':
            print(BORDA_SUPERIOR)
            print(f"{BORDA_LATERAL}{' PROGRAMA ENCERRADO. ATÉ LOGO! ':^40}{BORDA_LATERAL}")
            print(BORDA_INFERIOR)
            break
        else:
            print(BORDA_SUPERIOR)
            print(f"{BORDA_LATERAL}{' OPÇÃO INVÁLIDA! DIGITE 1, 2 OU 3. ':^40}{BORDA_LATERAL}")
            print(BORDA_INFERIOR)
            continue
        
        exibir_resultados(p1, p2, p3)
        
        if opcao != '3':
            print(BORDA_SUPERIOR)
            print(f"{BORDA_LATERAL} Deseja realizar outro cálculo? (s/n) {' ':>2}{BORDA_LATERAL}")
            print(BORDA_INFERIOR + "\n")
            if input(f"{' ':>15}Resposta: ").lower() != 's':
                print("\n" + BORDA_SUPERIOR)
                print(f"{BORDA_LATERAL}{' PROGRAMA ENCERRADO. ATÉ LOGO! ':^40}{BORDA_LATERAL}")
                print(BORDA_INFERIOR)
                break

if __name__ == "__main__":
    main()