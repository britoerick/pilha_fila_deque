import pilha as pilha

def fpQueue(value, array):
    array = pilha.push(value, array)
    return array


def fpDequeue(array):
    arrayAux = []
    for i in range(1, len(array)):
        pilha.push(array[i], arrayAux)

    return arrayAux


def fpPeek(array):
    array = array[::-1]
    return pilha.top(array)


