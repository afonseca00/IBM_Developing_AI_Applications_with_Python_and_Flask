"""
Defina uma função chamada 'add' que recebe dois argumentos, 'number1' e 'number2'.
O objetivo dessa função é somar os dois números e retornar o resultado.
"""
def add(number1, number2):
    """
    Retorne a soma de 'number1' e 'number2'.
    Esta linha calcula a adição dos dois números de entrada e produz o resultado.
    """
    return number1 + number2

# Inicialize a variável constante 'NUM1' com o valor 4.
# Constantes geralmente são escritas em letras maiúsculas para indicar que não devem ser alteradas.
NUM1 = 4

# Inicialize a variável 'num2' com o valor 5.
# Esta variável será usada como a segunda entrada para a função 'add'.
NUM2 = 5

# Chame a função 'add' com 'NUM1' e 'num2' como argumentos.
# O resultado dessa operação de adição é armazenado na variável 'total'.
TOTAL = add(NUM1, NUM2)

# Imprima uma string formatada que exibe a soma de 'NUM1' e 'num2'.
# O método 'format' é usado para inserir os valores de 'NUM1', 'num2' e 'total' na string.
print(f"A soma de {NUM1} e {NUM2} é {TOTAL}")
