import pilha as pilha
import fila as fila
import deque as deque
import fila_pilha as filapilha
from palindromo_pilha import palindromoPilha
from palindromo_deque import palindromoDeque

# Funções Pilha
print("********** Funções de Pilha **********")

# Push – insere um elemento na pilha
a = []
a = pilha.push('a', a)
print("Pilha push: {}".format(a))
a = pilha.push('b', a)
print("Pilha push: {}".format(a))
a = pilha.push('c', a)
print("Pilha push: {}".format(a))

# Pop – remove um elemento da pilha
a = pilha.pop(a)
print("Pilha pop: {}".format(a))

# Top – retorna o elemento no topo da pilha, sem removê-lo
print("Pilha top: {}".format(pilha.top(a)))

# isEmpty – verifica se a pilha está vazia ou não
print("Pilha isEmpty: {}".format(pilha.isEmpty(a)))

# size – retorna o número de elementos na pilha
print("Pilha size: {}".format(pilha.size(a)))

# Funções Fila
print("\n********** Funções de Fila **********")

# Queue– insere um elemento na fila
print("Fila queue: {}".format(a))
a = fila.queue('c', a)
print("Fila queue: {}".format(a))
a = fila.queue('d', a)
print("Fila queue: {}".format(a))

# Dequeue – remove um elemento da fila
a = fila.deque(a)
print("Fila dequeue: {}".format(a))

# Peek – retorna o elemento na frente da fila, sem removê-lo
print("Fila peek: {}".format(fila.peek(a)))

# isEmpty – verifica se a fila está vazia ou não
print("Fila isEmpty: {}".format(fila.isEmpty(a)))

# size – retorna o número de elementos na fila
print("Fila size: {}".format(fila.size(a)))

# Funções Deque
print("\n********** Funções de Deque **********")

# PushBack – Insere um novo elemento no fim do Deque
print("Deque pushback: {}".format(a))
a = deque.pushBack('e', a)
print("Deque pushback: {}".format(a))
a = deque.pushBack('f', a)
print("Deque pushback: {}".format(a))

# PushFront – Insere um novo elemento no início do Deque
a = deque.pushFront('a', a)
print("Deque pushfront: {}".format(a))
a = deque.pushFront('1', a)
print("Deque pushfront: {}".format(a))

# PopBack – Remove um elemento do fim do Deque
a = deque.popBack(a)
print("Deque popback: {}".format(a))
a = deque.popBack(a)
print("Deque popback: {}".format(a))

# PopFront – Remove um elemento do início do Deque
a = deque.popFront(a)
print("Deque popfront: {}".format(a))


# Funções Fila Utilizando Estrutura Pilha
print("\n********** Funções de Fila Utilizando Estrutura Pilha **********")

# Queue– insere um elemento na fila
print("Fila-Pilha queue: {}".format(a))
a = filapilha.fpQueue('e', a)
print("Fila-Pilha queue: {}".format(a))
a = filapilha.fpQueue('f', a)
print("Fila-Pilha queue: {}".format(a))

# Dequeue – remove um elemento da fila
a = filapilha.fpDequeue(a)
print("Fila-Pilha dequeue: {}".format(a))
a = filapilha.fpDequeue(a)
print("Fila-Pilha dequeue: {}".format(a))

# Peek – retorna o elemento na frente da fila, sem removê-lo
print("Fila-Pilha peek: {}".format(filapilha.fpPeek(a)))


# Função Palíndromo utilizando estrutura de pilha

print("\n********** Função de Palíndromo **********")

palin = ['ralo do dólar', 'até o poeta', 'tomarei café após a sopa']

for i in range(len(palin)):
    palindromoPilha(palin[i])
