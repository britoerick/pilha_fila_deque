import pilha as pilha
from unidecode import unidecode


def palindromoPilha(array):
    auxA = []
    auxB = []

    if pilha.isEmpty(array):
        print("String vazia")

    else:
        print("\n*************** teste de palíndromo ***************")
        print('Verificar: ' + array)

        # Remover acentos
        array = unidecode(array)

        # Deixar letras minúsculas, pois evita erro de comparação
        array = array.lower()

        # Verificar se contém espaço e remover
        if " " in array:
            array = array.replace(" ", "")

        loop = ((pilha.size(array)) - 1)
        for i in range(loop, -1, -1):
            auxA = pilha.push(array[i], auxA)
            auxB = pilha.push(array[loop - i], auxB)

        if auxA == auxB:
            print("Teste Verdadeiro")
            return True

        else:
            print("Teste Falso")
            return False
