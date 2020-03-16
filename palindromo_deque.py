import deque as deque
from unidecode import unidecode


def palindromoDeque(array):
    auxA = []
    auxB = []

    if len(array) <= 0:
        print("String vazia")

    else:
        print("*************** teste de palíndromo ***************")
        print('Verificar: ' + array)

        # Remover acentos
        array = unidecode(array)

        # Deixar letras minúsculas, pois evita erro de comparação
        array = array.lower()

        # Verificar se contém espaço e remover
        if " " in array:
            array = array.replace(" ", "")

        for i in range(len(array)):
            auxA = deque.pushFront(array[i], auxA)
            auxB = deque.pushBack(array[i], auxB)

        if auxA == auxB:
            print("Teste Verdadeiro")
            print("***************************************************")
            return True

        else:
            print("Teste Falso")
            print("***************************************************")
            return False



