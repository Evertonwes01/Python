# SET
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros) # [1, 2, 3, 4]

letras = set("abacaxi")
print(letras) # ["b", "a", "c", "x", "i"]

carros = set(("palio", "gol", "celta", "palio"))
print(carros) # ["gol", "celta", "palio"]

linguagens = {"python", "java", "python"}
print(linguagens)

# {}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}

# {}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}

# {}.diference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# {}.symmetric_diference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}

# {}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True   | Todos os elementos do conjunto_a pertence ao conjunto_b
conjunto_b.issubset(conjunto_a) # False  | Todos os elementos do conjunto_b pertence ao conjunto_a

# {}.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False | Todos os elementos do conjunto_b pertence ao conjunto_a
conjunto_b.issuperset(conjunto_a) # True  | Todos os elementos do conjunto_a pertence ao conjunto_b

# {}.isdisjoint
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True  | Todos os elementos do conjunto_a não pertence ao conjunto_b
conjunto_a.isdisjoint(conjunto_c) # False | Todos os elementos do conjunto_a não pertence ao conjunto_c

#{}.add

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42} |Ele não adiciona se já existe

# {}.clear
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear()
sorteio # {}

# {}.copy

sorteio = {1, 23}

sorteio # {1, 23}
teste = sorteio.copy()
teste # {1, 23}

# {}.discard
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.discard(1)
numeros.discard(45)

numeros # {2, 3, 4, 5, 6, 7, 8, 9} 

# in

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False
