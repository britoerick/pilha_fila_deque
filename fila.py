def isEmpty(array):
    if not array:
        return True
    else:
        return False


def size(array):
    return len(array)


def peek(array):
    return array[0:1]


def deque(array):
    return array[1:]


def queue(value, array):
    if type(array) is str:
        arrayAux = []
        for i in range(0, len(array)):
            arrayAux.append(array[i])

        arrayAux.append(value)
        return arrayAux
    else:
        array.append(value)
        return array

