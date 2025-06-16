# Constantes para bordas
BORDA_SUPERIOR = "╔════════════════════════════════════════════════════════╗"
BORDA_INFERIOR = "╚════════════════════════════════════════════════════════╝"
BORDA_LATERAL = "║"
BORDA_DIVISORIA = "╠════════════════════════════════════════════════════════╣"

def print_com_borda(texto: str):
    print(BORDA_SUPERIOR)
    for linha in texto.split("\n"):
        print(f"{BORDA_LATERAL} {linha:<54} {BORDA_LATERAL}")
    print(BORDA_INFERIOR)

def det2x2(matriz2):
    print_com_borda("Matriz escolhida:\n" + f"{matriz2[0]}\n{matriz2[1]}")
    print_com_borda("Passo a passo demonstrado\nMultiplicações")
    
    mul21 = matriz2[0][0] * matriz2[1][1]
    mul22 = matriz2[0][1] * matriz2[1][0]
    
    print_com_borda(f"Multiplicando {matriz2[0][0]} por {matriz2[1][1]}: {mul21}\n"
                    f"Multiplicando {matriz2[0][1]} por {matriz2[1][0]}: {mul22}")
    
    det2 = mul21 - mul22
    print_com_borda(f"Subtraindo {mul21} por {mul22}\nDeterminante: {det2}")
    return det2

def det3x3(matriz3, ordem=None):
    if ordem:
        print_com_borda(f"Calculando o {ordem}º Determinante 3x3")
    else:
        print_com_borda("Utilizaremos o método de Sarrus")
    
    print_com_borda(f"{matriz3[0]}\n{matriz3[1]}\n{matriz3[2]}")
    
    mul31 = matriz3[0][0] * matriz3[1][1] * matriz3[2][2]
    mul32 = matriz3[0][1] * matriz3[1][2] * matriz3[2][0]
    mul33 = matriz3[0][2] * matriz3[1][0] * matriz3[2][1]

    mul34 = matriz3[0][2] * matriz3[1][1] * matriz3[2][0]
    mul35 = matriz3[0][0] * matriz3[1][2] * matriz3[2][1]
    mul36 = matriz3[0][1] * matriz3[1][0] * matriz3[2][2]
    
    print_com_borda("Multiplicações\n"
        f"{matriz3[0][0]} * {matriz3[1][1]} * {matriz3[2][2]} = {mul31}\n"
        f"{matriz3[0][1]} * {matriz3[1][2]} * {matriz3[2][0]} = {mul32}\n"
        f"{matriz3[0][2]} * {matriz3[1][0]} * {matriz3[2][1]} = {mul33}\n"
        f"{matriz3[0][2]} * {matriz3[1][1]} * {matriz3[2][0]} = {mul34}\n"
        f"{matriz3[0][0]} * {matriz3[1][2]} * {matriz3[2][1]} = {mul35}\n"
        f"{matriz3[0][1]} * {matriz3[1][0]} * {matriz3[2][2]} = {mul36}")
    
    soma31 = mul31 + mul32 + mul33
    soma32 = mul34 + mul35 + mul36
    
    print_com_borda(f"Somas:\nDireta: {soma31}\nInversa: {soma32}")
    
    det3 = soma31 - soma32
    print_com_borda(f"Determinante: {det3}")
    return det3

def calculaCofator(elemento, numLinha, numColuna, ordem=None):
    somaC = numLinha + numColuna
    cofator = ((-1)**somaC) * elemento
    if ordem:
        print_com_borda(f"Calculando o {ordem}º Cofator")
    print_com_borda(f"Obtendo o cofator\n"
                    f"Soma dos índices: {somaC}\n"
                    f"(-1)^{somaC} * {elemento} = {cofator}")
    return cofator

def det4x4(matriz4):
    print_com_borda("Matriz escolhida:\n" +
        "\n".join([str(linha) for linha in matriz4]))
    print_com_borda("Utilizaremos o Teorema de Laplace\nBase: Linha 1")
    
    def submatriz(i):
        return [
            [matriz4[r][c] for c in range(4) if c != i]
            for r in range(1, 4)
        ]

    dets = []
    cofatores = []
    for i in range(4):
        m3 = submatriz(i)
        det_i = det3x3(m3, i + 1)  # Numeração dos determinantes
        cof = calculaCofator(det_i, 1, i + 1, i + 1)  # Numeração dos cofatores
        produto = matriz4[0][i] * cof
        dets.append(produto)
        cofatores.append((matriz4[0][i], cof))

    resultado = sum(dets)
    mults = "\n".join([f"{a} * {b} = {a * b}" for a, b in cofatores])
    print_com_borda("Multiplicações dos cofatores:\n" + mults)
    print_com_borda(f"Determinante final: {resultado}")

def menu():
    print_com_borda("Escolha o tipo de matriz:\n"
                    "4 - Matriz 4x4\n"
                    "3 - Matriz 3x3\n"
                    "2 - Matriz 2x2\n"
                    "1 - Sair")

def montarMatriz(numero):
    matriz = []
    for i in range(numero):
        linha = []
        for j in range(numero):
            while True:
                try:
                    valor = int(input(f"\nDigite o valor para ({i+1},{j+1}): "))
                    break
                except ValueError:
                    print("\nEntrada inválida! Por favor, digite um número inteiro.")
            linha.append(valor)
        matriz.append(linha)
    return matriz


def main():
    print_com_borda("Bem-vindo(a) ao Tutor de Determinantes!")
    menu()
    tipo = input("Seleção: ").strip()

    while tipo != "1":
        if tipo == "4":
            det4x4(montarMatriz(4))
        elif tipo == "3":
            det3x3(montarMatriz(3))
        elif tipo == "2":
            det2x2(montarMatriz(2))
        else:
            print_com_borda("Seleção inválida. Tente novamente.")
        menu()
        tipo = input("Nova seleção: ").strip()

    print_com_borda("Programa encerrado. Até logo!")

if __name__ == "__main__":
    main()
