def pushBack(value, array):
    if type(array) is str:
        arrayAux = []
        for i in range(0, len(array)):
            arrayAux.append(array[i])

        arrayAux.append(value)
        return arrayAux
    else:
        array.append(value)
        return array


def pushFront(value, array):
    arrayAux = [value]

    for i in range(0, len(array)):
        arrayAux.append(array[i])

    return arrayAux


def popBack(array):
    return array[:-1]


def popFront(array):
    return array[1:]


