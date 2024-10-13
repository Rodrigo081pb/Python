# No python assim como em qualquer outra linguagem vai utilizar tipo de dados
# Podem ser int = inteiro
# Podem ser float = decimal
# Podem ser complex = complexo
# Podem ser str = string
# Podem ser bool = Boolean
# Podem ser list = list como por exemplo ['Mônica', 'Ana', 'Bruno', 'Alice'] de fato é uma lista
# Podem ser tuple = tuple por exemplo (90, 79, 54, 32, 21)
# Podem ser dic = que se trata de um dicionario que utiliza chaves {'Camila': 1.65, 'Larissa': 1.60, 'Guilherme': 1.70}

# Partindo desde o início vale ressaltar o exemplo utilizando o tipo inteiro

# No python assim como em qualquer outra linguagem vai utilizar tipo de dados
# Podem ser int = inteiro
# Podem ser float = decimal
# Podem ser complex = complexo
# Podem ser str = string
# Podem ser bool = Boolean
# Podem ser list = list como por exemplo ['Mônica', 'Ana', 'Bruno', 'Alice'] de fato é uma lista
# Podem ser tuple = tuple por exemplo (90, 79, 54, 32, 21)
# Podem ser dic = que se trata de um dicionario que utiliza chaves {'Camila': 1.65, 'Larissa': 1.60, 'Guilherme': 1.70}

# Partindo desde o início vale ressaltar o exemplo utilizando o tipo inteiro

idade = 20
ano = 2010

print(type(idade))
print(type(ano))

# A resposta será imprimida como class 'int' que em outras palavras está se referindo a o tipo de classe que ela pertence que é do tipo inteiro

# Se falando do Decimal ou Float segue exemplo abaixo

altura = 1.73
peso = 78.500

print(type(peso))
print(type(altura))

# Que virá retornar como class float

# Já se falando do Complex ou complexo se trata de um tipo de dado utilizado para representar números complexos, normalmente cálculos geométricos e cientificos.

a = 10 + 16j
b = 3 + 80j

print(type(a))
print(type(b))

# Que vai retornar como Class complex

# Se falando da String ou str se refere ao texto por exemplo

marca = "Samsung"
modelo = "A54"

print("Eu possuo um ", marca, " do modelo ", modelo)
print("A string é do tipo: ", (type(marca)))

# Vai retornar str

# Bool ou boleano se trata do verdadeiro ou falso ou modelo lógico que nada mais é justamente o que foi dito no início

salario = True

if salario == True:
    print(
        "Fui pesquisar no sistema sobre o que Jorge falou que ele ganhava mais de 1000 reais e ele me retornou: ",
        salario,
    )
else:
    print("Jorge mentiu sobre o seu salário pois o sistema retornou: ", salario)

# Lista ou list ela agrupa um conjunto de elementos variados que podem conter todo tipo de dados utilizando o colchetes [] para demilitar a lista e virgulas para separar elementos

alunos = ["Mônica", "Ana", "Bruno", "Alice"]
notas = [10, 8.5, 7.8, 8.0]

print(type(alunos))
print(type(notas))
