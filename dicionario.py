# Estrutura de criação de dicionario
pessoa = {"nome": "Everton", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["nome"] # "Guilherme"

# Estrutura de criação de dicionario aninhados

registros = {
    "everton@gmail.com": {"nome": "Everton", "telefone": "3333-2221"},
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3453-2321"},
    "luana@gmail.com": {"nome": "Luana", "telefone": "3333-0121"},
    "fernanda@gmail.com": {"nome": "Fernanda", "telefone": "3783-2991", "extra": {"a": 1}}
}

telefone = registros["luana@gmail.com"]["telefone"] # "3333-0121"
print(telefone)

extra = registros["fernanda@gmail.com"]["extra"]
print(extra)

#iterar dicionario

for chave in registros:
    print(chave,registros[chave])

print("==================================================================")

for chave, valor in registros.items():
    print(chave,valor)

# Metodos e classes do Dicionario
    
pessoa["nome"] = "Maria"
pessoa # "Maria"

# MÉTODOS

#{}.clear

registros = {
    "everton@gmail.com": {"nome": "Everton", "telefone": "3333-2221"},
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3453-2321"},
    "luana@gmail.com": {"nome": "Luana", "telefone": "3333-0121"},
    "fernanda@gmail.com": {"nome": "Fernanda", "telefone": "3783-2991", "extra": {"a": 1}}
}

registros.clear()
registros # {} >> AGORA ESTÁ VAZIA

#{}.copy

registros = {
    "everton@gmail.com": {"nome": "Everton", "telefone": "3333-2221"},
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3453-2321"},
    "luana@gmail.com": {"nome": "Luana", "telefone": "3333-0121"},
    "fernanda@gmail.com": {"nome": "Fernanda", "telefone": "3783-2991", "extra": {"a": 1}}
}

copia = registros.copy()
copia # TODOS OS REGISTROS FORAM COPIADOS PARA O DICIONARIO CÓPIA

#{}.fromkeys | CRIA UM DICIONARIO SÓ COM CHAVES 

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None} >> SEM VALOR INSERIDO

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": vazio, "telefone": vazio} >> COM VALOR PADRÃO INSERIDO

# {}.get | ACESSAR VALOR NO DICIONARIO

contatos = {
    "guilherme@gmail.com": {"Nome": "Guilherme", "Telefone": "3455-0014"}
}

#contatos[chave] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"Nome": "Guilherme", "Telefone": "3455-0014"}}

# {}.items | Retorna uma lista de dicionario

contatos = {
    "guilherme@gmail.com": {"Nome": "Guilherme", "Telefone": "3455-0014"}
}

contatos.items() # dict_items([("guilherme@gmail.com": {"Nome": "Guilherme", "Telefone": "3455-0014")])

# {}.keys | Retorna só as chaves dos dicionarios

contatos = {"Nome": "Guilherme", "Telefone": "3455-0014"}

print("==========================================")
print(contatos.keys()) # {'Nome', 'Telefone'}

# {}.pop

contatos = {
    "guilherme@gmail.com": {"Nome": "Guilherme", "Telefone": "3455-0014"}
}
contatos.pop("guilherme@gmail.com") # Se encontrar a chave para remover retorna a chave com os valores
contatos.pop("guilherme@gmail.com", {}) # se nao encontrar retorna {} vazio


